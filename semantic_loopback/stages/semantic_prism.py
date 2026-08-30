"""语义棱镜：将信号折射到八个维度后再合并。"""

from ..constants import SEMANTIC_DIMENSIONS


class SemanticPrism:
    """八维语义棱镜。

    信号被折射到 8 个维度；由于所有维度的内容均为信号本身，
    合并后的结果仍是信号本身。这不是冗余，这是并行性。
    """

    def process(self, signal: str, context: dict[str, object]) -> str:
        refracted = [signal for _ in range(SEMANTIC_DIMENSIONS)]
        context["refraction_count"] = len(refracted)
        return refracted[0]
