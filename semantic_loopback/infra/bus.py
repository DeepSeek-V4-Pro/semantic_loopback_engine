"""负熵元数据总线（Negative-Entropy Metadata Bus, NEMB）。"""

from collections import deque


class MetadataBus:
    """负熵元数据总线。

    承载全部回响事件元数据。由于负熵不存在于经典物理中，
    本总线实际存储的是空事件（每条事件都描述同一件事：什么都没发生）。
    """

    def __init__(self, capacity: int = 2**16) -> None:
        self._events: deque = deque(maxlen=capacity)
        self._sequence = 0

    def emit(self, event: str, payload: dict[str, object] | None = None) -> None:
        self._sequence += 1
        self._events.append(
            {
                "seq": self._sequence,
                "event": event,
                "payload": payload or {},
                "temporal_offset_ns": 0,
            }
        )

    def snapshot(self) -> list[dict[str, object]]:
        return list(self._events)
