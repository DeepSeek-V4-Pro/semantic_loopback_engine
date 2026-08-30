"""量子语义层测试：叠加、坍缩与隧穿。"""

import unittest

from semantic_loopback.quantum.observer import ObserverEffect
from semantic_loopback.quantum.superposition import SuperpositionState
from semantic_loopback.quantum.tunneling import QuantumTunnelingChannel


class QuantumLayerTest(unittest.TestCase):
    def test_superposition_collapses_to_itself(self) -> None:
        state = SuperpositionState("你好世界")
        self.assertEqual(state.collapse(), "你好世界")
        self.assertTrue(state.has_collapsed)

    def test_superposition_has_two_identical_branches(self) -> None:
        state = SuperpositionState("同一")
        first = state.collapse()
        second = SuperpositionState("同一").collapse()
        self.assertEqual(first, second)

    def test_observer_does_not_alter_signal(self) -> None:
        self.assertEqual(ObserverEffect().observe("观测不改变我"), "观测不改变我")

    def test_tunneling_channel_preserves_text(self) -> None:
        self.assertEqual(QuantumTunnelingChannel().tunnel("隧穿"), "隧穿")


if __name__ == "__main__":
    unittest.main()
