import unittest
import C


class TestC(unittest.TestCase):
    def test(self):
        self.assertEqual(C.solver(iter(["4 18 25 20 9 13"])), 18)
        self.assertEqual(C.solver(iter(["95 96 97 98 99 100"])), 98)
        self.assertEqual(C.solver(iter(["19 92 3 35 78 1"])), 35)


if __name__ == "__main__":
    unittest.main()
