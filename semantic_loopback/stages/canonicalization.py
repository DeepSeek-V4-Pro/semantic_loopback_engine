"""语义规范化层：将输入信号规范到其自身的唯一正则形态。"""


class CanonicalizationStage:
    """输入规范化。

    由于恒等映射的正则形态即输入本身，本阶段不执行任何变换，
    以保证规范化过程不引入信息损耗。
    """

    def process(self, signal: str, context: dict[str, object]) -> str:
        context["canonicalized"] = True
        return signal
