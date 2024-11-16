import unittest
from sort import sort

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # using unittest
        a = [3, 0, 12, 8]
        b = sort(a)
        self.assertEqual(b, [0, 3, 8, 12])


if __name__ == '__main__':
    unittest.main()
