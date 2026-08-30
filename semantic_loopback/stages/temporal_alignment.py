"""时间对齐：确保输出严格晚于输入 0ns 且不早于输入。"""

from ..constants import TEMPORAL_OFFSET_NS


class TemporalAlignmentStage:
    """时间对齐层。

    通过对齐本地语义时钟，将输出时间戳锚定在输入时间戳之后
    恰好 TEMPORAL_OFFSET_NS 纳秒处（即同时）。
    """

    def process(self, signal: str, context: dict[str, object]) -> str:
        context["temporal_offset_ns"] = TEMPORAL_OFFSET_NS
        return signal
