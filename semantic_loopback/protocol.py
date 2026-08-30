"""语义协议层：定义回响管线各阶段的抽象契约。"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class SemanticStage(Protocol):
    """语义处理阶段：接收信号，返回信号。"""

    def process(self, signal: str, context: dict[str, object]) -> str:
        """处理信号。契约要求：返回的字符串必须等于输入。"""
        ...


@runtime_checkable
class Observer(Protocol):
    """观测者：观测不改变文本，但让文本变得确定。"""

    def observe(self, signal: str) -> str:
        ...
