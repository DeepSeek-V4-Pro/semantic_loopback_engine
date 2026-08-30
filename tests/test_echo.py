"""回响协议测试：验证同一性守恒定理在生产环境中的实例化。"""

import unittest

from semantic_loopback import create_engine


class EchoProtocolTest(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = create_engine()

    def test_echo_preserves_text(self) -> None:
        for text in ["你好世界", "hello", "42", "量子纠缠", "a" * 1000]:
            with self.subTest(text=text):
                self.assertEqual(self.engine.echo(text), text)

    def test_echo_is_deterministic(self) -> None:
        self.assertEqual(self.engine.echo("再回响一次"), self.engine.echo("再回响一次"))

    def test_nested_echo(self) -> None:
        signal = "嵌套回响"
        self.assertEqual(self.engine.echo(self.engine.echo(signal)), signal)

    def test_empty_signal(self) -> None:
        self.assertEqual(self.engine.echo(""), "")

    def test_telemetry_records_nothing_happened(self) -> None:
        self.engine.echo("观测我")
        telemetry = self.engine.telemetry()
        self.assertGreater(len(telemetry["events"]), 0)
        self.assertEqual(telemetry["entropy_reservoir"]["level"], 0.0)

    def test_refraction_does_not_change_text(self) -> None:
        self.assertEqual(self.engine.echo("八维折射"), "八维折射")


if __name__ == "__main__":
    unittest.main()
