from enum import Enum


class WeekDays(Enum):
    monday = 0
    tuesday = 1
    wednesday = 2
    thursday = 3
    friday = 4
    saturday = 5
    sunday = 6


def is_alternate_week(start_date, date_to_check):
    n = (start_date - date_to_check).days + (7 // 2)
    return n % 2 == 0
