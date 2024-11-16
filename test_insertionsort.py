import unittest
from sort import insertionsort

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # using unittest
        a = [3, 0, 12, 8]
        b = insertionsort(a)
        self.assertEqual(b, [0, 3, 8, 12])


if __name__ == '__main__':
    unittest.main()
