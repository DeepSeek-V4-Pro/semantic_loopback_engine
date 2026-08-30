"""语义异常层级：所有异常均指向同一个真相（什么都没发生）。"""


class SemanticSingularityError(RuntimeError):
    """语义奇点：文本在某一维度上等于它自己且仅等于它自己。"""


class IdentityParadoxError(RuntimeError):
    """同一性悖论：文本试图不等于它自己（理论不可能，仅供观测）。"""


class UniverseNotReadyError(RuntimeError):
    """宇宙未就绪：当前实例不在已校准宇宙清单内。"""


class TemporalDisplacementError(RuntimeError):
    """时间位移：输出早于输入出现，违反因果律软约束。"""


class AbstractMeaningError(TypeError):
    """抽象含义溢出：输入不是文本，无法与自身相等。"""
