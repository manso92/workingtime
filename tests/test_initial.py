import unittest

import numpy as np

class InitialTest(unittest.TestCase):

    # def setUp(self): could be defined for set up before any test

    def test_sample(self):
        np.testing.assert_allclose([0], [0])


if __name__ == '__main__':
    print()
    unittest.main()
