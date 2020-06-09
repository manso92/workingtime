import unittest

import numpy as np
from datetime import datetime, time, timedelta
from workingtime import WTime


class WTimeTest(unittest.TestCase):

    def test_seconds(self):
        np.testing.assert_equal(WTime(10).seconds(), 36000)
        np.testing.assert_equal(WTime(10, 10).seconds(), 36600)
        np.testing.assert_equal(WTime(10, 10, 20).seconds(), 36620)

    def test_from_seconds(self):
        np.testing.assert_equal(WTime.from_seconds(36000), WTime(10))
        np.testing.assert_equal(WTime.from_seconds(36600), WTime(10, 10))
        np.testing.assert_equal(WTime.from_seconds(36620), WTime(10, 10, 20))

    def test_from_time(self):
        np.testing.assert_equal(WTime.from_seconds(36000), time(10))
        np.testing.assert_equal(WTime.from_seconds(36600), time(10, 10))
        np.testing.assert_equal(WTime.from_seconds(36620), time(10, 10, 20))

    def test_from_dt(self):
        np.testing.assert_equal(WTime.from_seconds(36000),
                                WTime.from_dt(datetime(2020, 10, 10, 10)))
        np.testing.assert_equal(WTime.from_seconds(36600),
                                WTime.from_dt(datetime(2020, 10, 10, 10, 10)))
        np.testing.assert_equal(WTime.from_seconds(36620),
                                WTime.from_dt(datetime(2020, 10, 10,
                                                       10, 10, 20)))

    def test_sub(self):
        np.testing.assert_equal(WTime(10) - WTime(10), timedelta(0))
        np.testing.assert_equal(WTime(11) - WTime(10), timedelta(minutes=60))
        np.testing.assert_equal(WTime(9) - WTime(10), timedelta(hours=-1))

    def test_rsub(self):
        np.testing.assert_equal(WTime(10).__rsub__(WTime(10)),
                                timedelta(0))
        np.testing.assert_equal(WTime(10).__rsub__(WTime(11)),
                                timedelta(minutes=60))
        np.testing.assert_equal(WTime(10).__rsub__(WTime(9)),
                                timedelta(hours=-1))