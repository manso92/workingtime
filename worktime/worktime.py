import pandas as pd
from datetime import time

class WorkTime:
    def __init__(self, workhours=[],  holidays=[]):
        self.holidays = holidays
        self.workhours = workhours
