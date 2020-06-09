import unittest

import numpy as np
from datetime import datetime
from workingtime.misc import _is_overlapping, _is_overlapping_bis
from workingtime.misc import *


class MiscTest(unittest.TestCase):

    def test_dates_between_dates(self):
        now = datetime.now()
        day = timedelta(1)

        np.testing.assert_array_equal(
            dates_between_dates(now, now), [])
        np.testing.assert_array_equal(
            dates_between_dates(now, now + day), [])
        np.testing.assert_array_equal(
            dates_between_dates(now, now + 2 * day),
            [now + day])
        # If the start is later than end, no dates between
        np.testing.assert_array_equal(
            dates_between_dates(now, now - 2 * day),
            [])


    def test_is_overlapping(self):
        np.testing.assert_equal(_is_overlapping(1, 10, 11, 20), False)
        np.testing.assert_equal(_is_overlapping(1, 10, 10, 20), True)
        np.testing.assert_equal(_is_overlapping(1, 11, 10, 20), True)
        np.testing.assert_equal(_is_overlapping(1, 11, 2, 8), True)
        np.testing.assert_equal(_is_overlapping(10, 20, 1, 11), True)


    def test_is_overlapping_bis(self):
        np.testing.assert_equal(_is_overlapping_bis(1, 10, 11, 20), False)
        np.testing.assert_equal(_is_overlapping_bis(1, 10, 10, 20), True)
        np.testing.assert_equal(_is_overlapping_bis(1, 11, 10, 20), True)
        np.testing.assert_equal(_is_overlapping_bis(1, 11, 2, 8), True)
        np.testing.assert_equal(_is_overlapping_bis(10, 20, 1, 11), True)


    def test_overlap(self):

        np.testing.assert_equal(overlap(10, 20), 10)
        np.testing.assert_equal(overlap(10, 20, 11), 9)
        np.testing.assert_equal(overlap(10, 20, None, 11), 1)
        np.testing.assert_equal(overlap(10, 10, 1, 11).seconds, 0)
        np.testing.assert_equal(overlap(1, 10, 1, 1).seconds, 0)
        np.testing.assert_equal(overlap(10, 10, 1, 1).seconds, 0)
        np.testing.assert_equal(overlap(10, 11, 1, 2).seconds, 0)
        np.testing.assert_equal(overlap(1, 10, 3, 15), 7)
