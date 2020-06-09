import datetime as dt
from datetime import timedelta


class WTime(dt.time):
    def seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    @staticmethod
    def from_seconds(seconds):
        secs = seconds % 60
        mins = int(seconds / 60) % 60
        hours = int(seconds / 3600) % 24
        return WTime(hours, mins, secs)

    @staticmethod
    def from_time(dtime):
        return WTime(dtime.hour, dtime.minute, dtime.second)

    @staticmethod
    def from_dt(dtime):
        return WTime.from_time(dtime.time())

    def __sub__(self, other):
        return timedelta(seconds=self.seconds() - other.seconds())

    def __rsub__(self, other):
        return WTime.from_time(other) - self