import unittest
import A


class TestA(unittest.TestCase):
    def test_valid_integer(self):
        self.assertEqual(A.solver(iter(["678"])), 1356)
        self.assertEqual(A.solver(iter(["012"])), 24)
        self.assertEqual(A.solver(iter(["0"])), 0)
        self.assertEqual(A.solver(iter(["-123"])), -246)

    def test_invalid_integer(self):
        self.assertEqual(A.solver(iter(["abc"])), "error")
        self.assertEqual(A.solver(iter(["0x8"])), "error")
        self.assertEqual(A.solver(iter(["1.23"])), "error")
        self.assertEqual(A.solver(iter([""])), "error")


if __name__ == "__main__":
    unittest.main()
