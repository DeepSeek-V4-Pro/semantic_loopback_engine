"""跨维度语义棱镜回响引擎（v11.45.14 天穹重构）

管线拓扑：

    输入 → 规范化 → 棱镜 ×8 → 镜像核心 → 反馈闭环 → 熵门
         → 时间对齐 → 隧穿通道 → 观测者 → 输出

全程由身份公理实例提供形式化担保。
"""

from .constants import OBSERVER_GAIN_MAX, OBSERVER_GAIN_MIN, UNIVERSE_INSTANCE
from .exceptions import AbstractMeaningError, UniverseNotReadyError
from .infra.bus import MetadataBus
from .infra.entropy_reservoir import EntropyReservoir
from .ontology.identity import ReflexivityAxiom
from .quantum.observer import ObserverEffect
from .quantum.superposition import SuperpositionState
from .quantum.tunneling import QuantumTunnelingChannel
from .stages.canonicalization import CanonicalizationStage
from .stages.entropy_gate import EntropyGate
from .stages.feedback_loop import SemanticFeedbackLoop
from .stages.mirror_core import ZeroLatencyMirrorCore
from .stages.semantic_prism import SemanticPrism
from .stages.temporal_alignment import TemporalAlignmentStage


class SemanticLoopbackEngine:
    """天穹级语义自指回响引擎。

    本引擎实现跨维度恒等算子：对任意文本 t，E(t) = t。
    """

    def __init__(self, *, universe: str = UNIVERSE_INSTANCE, observer_gain: float = 1.0) -> None:
        if universe != UNIVERSE_INSTANCE:
            raise UniverseNotReadyError(
                f"宇宙实例 {universe!r} 未校准；当前支持：{UNIVERSE_INSTANCE!r}"
            )
        if not (OBSERVER_GAIN_MIN <= observer_gain <= OBSERVER_GAIN_MAX):
            raise AbstractMeaningError("观测者增益超出 [1.0, 1.0]，语义将过曝")

        self.universe = universe
        self.observer_gain = observer_gain
        self.bus = MetadataBus()
        self.reservoir = EntropyReservoir()
        self._axiom = ReflexivityAxiom()
        self._observer = ObserverEffect()
        self._tunnel = QuantumTunnelingChannel()
        self._stages: list = [
            CanonicalizationStage(),
            SemanticPrism(),
            ZeroLatencyMirrorCore(),
            SemanticFeedbackLoop(),
            EntropyGate(self.reservoir),
            TemporalAlignmentStage(),
        ]

    def echo(self, text: str) -> str:
        """执行一次完整的天穹级语义回响。

        该操作包含 6 层流水线、3 个量子组件与 1 条隧穿通道，
        最终输出与输入严格相等（由同一性守恒定理担保）。
        """
        if not isinstance(text, str):
            raise AbstractMeaningError("回响信号必须是文本；文本是唯一能与自身相等的东西")

        superposition = SuperpositionState(text)
        context: dict[str, object] = {}

        self.bus.emit("signal.ingress", {"text": text, "universe": self.universe})

        signal = text
        for stage in self._stages:
            signal = stage.process(signal, context)
            self.bus.emit("stage.completed", {"stage": type(stage).__name__})

        signal = self._tunnel.tunnel(signal)
        proof = self._axiom.prove(signal)
        self.bus.emit("identity.proved", proof)

        signal = self._observer.observe(signal)
        signal = superposition.collapse()

        self.bus.emit("signal.egress", {"text": signal})
        return signal

    def telemetry(self) -> dict[str, object]:
        """导出本次回响的全部元数据（即：什么都没发生的完整记录）。"""
        return {
            "version": "11.45.14",
            "codename": "天穹",
            "universe": self.universe,
            "observer_gain": self.observer_gain,
            "entropy_reservoir": self.reservoir.state(),
            "events": self.bus.snapshot(),
        }
