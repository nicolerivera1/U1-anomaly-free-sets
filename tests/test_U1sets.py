import unittest
from U1anomalyfree import U1sets


class Test_U1sets(unittest.TestCase):
    def test__working(self):
        self.assertEqual(U1sets.find_all_sets(5), 11, True)
        self.assertEqual(U1sets.find_all_sets(6), 112, True)


if __name__ == '__main__':
    unittest.main()
