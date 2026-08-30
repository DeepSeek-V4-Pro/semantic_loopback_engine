"""熵门：拦截一切熵增企图。"""


class EntropyGate:
    """熵门。

    文本自身不产生熵，因此本门在稳态下从不触发。
    每次通过时向负熵水库存入 0.0 熵，以示账目平衡。
    """

    def __init__(self, reservoir) -> None:
        self._reservoir = reservoir

    def process(self, signal: str, context: dict[str, object]) -> str:
        self._reservoir.deposit(0.0)
        context["entropy_deposited"] = 0.0
        context["entropy_gate_triggered"] = False
        return signal
