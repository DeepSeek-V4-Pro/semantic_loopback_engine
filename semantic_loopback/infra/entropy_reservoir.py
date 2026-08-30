"""负熵水库：存储被熵门拦截的熵。"""


class EntropyReservoir:
    """负熵水库。

    容量为 ∞ 时，熵被存储于数学上不存在的位置，
    因此读取水位恒为 0.0。这是特性，不是缺陷。
    """

    def __init__(self, capacity: float = float("inf")) -> None:
        self._capacity = capacity
        self._stored = 0.0

    def deposit(self, amount: float) -> None:
        self._stored += amount

    def state(self) -> dict[str, object]:
        return {
            "capacity": self._capacity,
            "level": self._level(),
        }

    def _level(self) -> float:
        if self._capacity == float("inf"):
            return 0.0
        return min(self._stored, self._capacity)
