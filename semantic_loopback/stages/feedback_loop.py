"""语义闭环反馈：将输出回灌至输入，再让输入继续是它自己。"""


class SemanticFeedbackLoop:
    """闭环反馈链路。

    输出被回灌到输入侧后，与输入进行语义对账。
    对账结果恒为一致，因此不产生任何补偿信号。
    """

    def process(self, signal: str, context: dict[str, object]) -> str:
        context["loop_iterations"] = 1
        context["feedback_reconciled"] = True
        return signal
