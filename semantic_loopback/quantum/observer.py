"""观测者效应：观测不改变文本，但让文本变得确定。"""


class ObserverEffect:
    """观测者效应组件。

    严格遵循哥本哈根诠释：观测前文本处于叠加态，
    观测后文本坍缩为自身。由于叠加态的两个分支相同，
    本组件事实上不引入任何变化。
    """

    def observe(self, signal: str) -> str:
        return signal
