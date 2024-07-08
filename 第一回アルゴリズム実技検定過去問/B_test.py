import unittest
import B


class TestDoubleOrError(unittest.TestCase):
    def test(self):
        self.assertEqual(
            B.solver(
                iter(["10", "9", "10", "3", "100", "100", "90", "80", "10", "30", "10"])
            ),
            [
                "up 1",
                "down 7",
                "up 97",
                "stay",
                "down 10",
                "down 10",
                "down 70",
                "up 20",
                "down 20",
            ],
        )


if __name__ == "__main__":
    unittest.main()
