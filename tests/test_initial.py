import unittest

import numpy as np
from datetime import timedelta, datetime
from workingtime.workingtime import _dates_between_dates
from workingtime import WorkingTime, Time


class DatesBetweenDates(unittest.TestCase):

    def test_normal_use(self):
        now = datetime.now()
        day = timedelta(1)


        np.testing.assert_array_equal(
            _dates_between_dates(now, now + 2 * day),
            [now + day],
            "Error finding day between two non correlative days"
        )
        np.testing.assert_array_equal(
            _dates_between_dates(now, now + 4 * day),
            [now + x * day for x in range(1, 4)],
            "Error finding day between two non correlative days"
        )

    def test_same_dates(self):
        now = datetime.now()
        day = timedelta(1)

        np.testing.assert_array_equal(
            _dates_between_dates(now, now), [],
            "Error calculating empty distance"
        )

    def test_consecutive_dates(self):
        now = datetime.now()
        day = timedelta(1)

        np.testing.assert_array_equal(
            _dates_between_dates(now, now + day), [],
            "Error calculating consecutive dates"
        )


class Initialclass (unittest.TestCase):
    def test_another_test(self):
        wt = WorkingTime()
        np.testing.assert_equal(
            wt.working_time(datetime(2020, 10, 3, 1),
                           datetime(2020, 10, 4, 23),
                           (Time(22, 0), Time(0, 30))).total_seconds(),
            (2.5 + 1) * 3600)


if __name__ == '__main__':
    print()
    unittest.main()
