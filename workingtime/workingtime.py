from .misc import *
from .wtime import WTime


class WorkingTime:
    def __init__(self, weekends=None, holidays=None):
        # TODO check the variables
        self.weekends = weekends
        self.holidays = holidays

    def working_time(self, start, end, work_hours=None):
        if work_hours is None:
            work_hours = (WTime(8), WTime(16))

        work_hours = (WTime.from_time(work_hours[0]),
                      WTime.from_time(work_hours[1]))

        # If start > end, workingtime will be negative
        if start > end:
            return -1 * self.working_time(end, start, work_hours)

        # If the day changes between your workhours, its easier to calculate
        # the time your note working and substract
        if work_hours[0] > work_hours[1]:
            return ((end - start) -
                    self.working_time(start, end,
                                      tuple(reversed(work_hours))))

        # If the start time and the end time are the same we
        # return the workhours * days between. But it can't be done
        # like this because start date or end date could be weekend or holiday

        if start.date() == end.date():
            # TODO implementar esta  cosica
            return overlap(WTime.from_dt(start), WTime.from_dt(end), *work_hours)

        middle_time = (len(dates_between_dates(start, end)) *
                       (work_hours[1] - work_hours[0]))

        return (overlap(*work_hours, WTime.from_dt(start)) +
                middle_time +
                overlap(*work_hours, None, WTime.from_dt(end)))
