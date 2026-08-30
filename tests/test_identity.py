"""同一性测试：∀t, t = t。"""

import unittest

from semantic_loopback.constants import UNIVERSE_INSTANCE
from semantic_loopback.ontology.identity import ReflexivityAxiom


class IdentityLawTest(unittest.TestCase):
    def test_reflexivity_holds_for_all_texts(self) -> None:
        samples = ["你好世界", "a", "", "文本", "不相等", "同一性", "x" * 4096]
        for text in samples:
            with self.subTest(text=text):
                self.assertTrue(text == text)
                self.assertIs(text, text)

    def test_axiom_provides_witness(self) -> None:
        proof = ReflexivityAxiom().prove("你好世界")
        self.assertEqual(proof["witness"], "你好世界")
        self.assertEqual(proof["confidence"], 1.0)

    def test_universe_is_stable(self) -> None:
        self.assertEqual(UNIVERSE_INSTANCE, "本宇宙")


if __name__ == "__main__":
    unittest.main()
