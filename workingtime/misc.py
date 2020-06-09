import pandas as pd
from datetime import timedelta
from .wtime import WTime


def dates_between_dates(start, end):
    return list(pd.date_range(start + timedelta(1),
                              end - timedelta(1),
                              freq='d'))


def _is_overlapping(x1, x2, y1, y2):
    return not (x1 > y2 or y1 > x2)


def _is_overlapping_bis(x1, x2, y1, y2):
    return max(x1, y1) <= min(x2, y2)


def overlap(x1, x2, y1=None, y2=None):
    if y1 is None and y2 is None:
        return x2 - x1

    y1 = x1 if y1 is None else y1
    y2 = x2 if y2 is None else y2

    if x1 == x2 or y1 == y2 or not _is_overlapping(x1, x2, y1, y2):
        return timedelta(0)

    return min(x2, y2) - max(x1, y1)
