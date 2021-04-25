from datetime import time

GENERATED_WEEKS = 4
DEFAULT_NUMBER_OF_SLOTS = 5
DEFAULT_FREQUENCY = "weekly"
DEFAULT_SPECIAL_ITEMS = True

SLOTS_CONFIG = [
    {
        "name": "morning",
        "start_time": time(hour=7),
        "end_time": time(hour=12),
        "monday": {},
        "tuesday": {},
        "wednesday": {"special_item": False},
        "thursday": {},
        "friday": {
            "frequency": "fortnight",
        },
        "saturday": {},
        "sunday": {},
    },
    {
        "name": "afternoon",
        "start_time": time(hour=12),
        "end_time": time(hour=17),
        "monday": {},
        "tuesday": {},
        "wednesday": {"special_item": False},
        "thursday": {},
        "friday": {},
        "saturday": {},
        "sunday": {},
    },
    {
        "name": "evening",
        "start_time": time(hour=17),
        "end_time": time(hour=22),
        "monday": {},
        "tuesday": {},
        "wednesday": {"special_item": False},
        "thursday": {},
        "friday": {},
        "saturday": {},
        "sunday": {},
    },
]
