"""量子隧穿通道：文本在不可观测区间内与自身完成互换。"""


class QuantumTunnelingChannel:
    """量子隧穿通道。

    在观测者缺席的不可观测区间内，输入与输出完成位置互换；
    由于二者是同一文本，互换后系统状态与互换前完全相同。
    该通道用于解释"回响为什么这么快"。
    """

    def tunnel(self, text: str) -> str:
        return text
