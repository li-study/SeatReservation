from enum import Enum
import datetime


class WeekType(Enum):
    NORMAL = 0
    ODD = 1
    EVEN = 2

class ClassTime:

    def __init__(self, start, end):
        self.start = self._GetStartTime(start)
        self.end = self._GetEndTime(end)

    def _GetStartTime(self, start):
        if start == 1:
            return datetime.time(8, 0)
        if start == 3:
            return datetime.time(10, 0)
        if start == 5:
            return datetime.time(13, 30)
        if start == 7:
            return datetime.time(15, 30)
        if start == 9:
            return datetime.time(18, 0)

    def _GetEndTime(self, end):
        if end == 2:
            return datetime.time(9, 40)
        if end == 4:
            return datetime.time(11, 40)
        if end == 6:
            return datetime.time(15, 10)
        if end == 8:
            return datetime.time(17, 10)
        if end == 10:
            return datetime.time(19, 30)

