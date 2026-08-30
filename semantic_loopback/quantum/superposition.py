"""量子叠加：文本在观测前同时处于"是它自己"和"依然是它自己"的叠加。"""


class SuperpositionState:
    """语义叠加态。

    两个基态振幅均为 1.0，对应两种观测结果："它自己"与"它自己"。
    坍缩操作不会丢失信息，因为信息在两态中完全相同。
    """

    def __init__(self, text: str) -> None:
        self._amplitudes = [text, text]
        self._collapsed = False

    def collapse(self) -> str:
        """执行观测坍缩，返回确定的文本。"""
        self._collapsed = True
        return self._amplitudes[0]

    @property
    def has_collapsed(self) -> bool:
        return self._collapsed
