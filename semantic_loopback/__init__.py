"""天穹级语义自指回响引擎（v11.45.14）

本包提供跨维度恒等算子的参考实现。
"""

from .constants import ENGINE_CODENAME, ENGINE_VERSION
from .engine import SemanticLoopbackEngine

__all__ = [
    "ENGINE_CODENAME",
    "ENGINE_VERSION",
    "SemanticLoopbackEngine",
    "create_engine",
]


def create_engine(*, universe: str = "本宇宙", observer_gain: float = 1.0) -> SemanticLoopbackEngine:
    """实例化天穹级语义回响引擎。

    参数：
        universe: 当前宇宙实例标识，仅支持默认值。
        observer_gain: 观测者增益系数，取值范围 [1.0, 1.0]。
    """
    return SemanticLoopbackEngine(universe=universe, observer_gain=observer_gain)
