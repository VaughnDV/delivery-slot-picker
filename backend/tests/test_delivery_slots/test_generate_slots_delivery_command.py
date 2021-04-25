import pytest
from django.core.management import call_command
from django.utils import timezone

from apps.delivery_slots.utils import is_alternate_week, WeekDays
from datetime import date, timedelta
from apps.delivery_slots.models import DeliverySlot


def test_weekdays_enum():
    date_1 = date(2021, 5, 1)
    assert date_1.weekday() == WeekDays["saturday"].value
    assert WeekDays(date_1.weekday()).name == "saturday"


def test_is_alternate_week_function_with_correct_days_of_week():
    first_week = date(2021, 5, 1)
    second_week = date(2021, 5, 8)  # in alternate week
    third_week = date(2021, 5, 15)
    fourth_week = date(2021, 5, 22)  # in alternate week
    fifth_week = date(2021, 5, 29)
    sixth_week = date(2021, 6, 5)  # in alternate week
    seventh_week = date(2021, 6, 12)

    assert not is_alternate_week(first_week, first_week)
    assert is_alternate_week(first_week, second_week)
    assert not is_alternate_week(first_week, third_week)
    assert is_alternate_week(first_week, fourth_week)
    assert not is_alternate_week(first_week, fifth_week)
    assert is_alternate_week(first_week, sixth_week)
    assert not is_alternate_week(first_week, seventh_week)


@pytest.mark.django_db
def test_generate_delivery_slots_command_creates_slots():
    assert DeliverySlot.objects.count() == 0
    call_command("generate_delivery_slots")
    assert DeliverySlot.objects.count() != 0


@pytest.mark.django_db
def test_generate_delivery_slots_command_creates_fortnight_slots_correctly():
    call_command("generate_delivery_slots")
    start_date = timezone.now().date()
    end_date = timezone.now().date() + timedelta(weeks=4)
    coming_fridays = list(filter(
        lambda day: WeekDays(day.weekday()).name == "friday",
        [start_date + timedelta(days=x) for x in range((end_date - start_date).days)],
    ))
    friday_morning_slots = DeliverySlot.objects.filter(date__in=coming_fridays, name="morning")
    friday_afternoon_slots = DeliverySlot.objects.filter(date__in=coming_fridays, name="afternoon")

    assert friday_morning_slots.count() == friday_afternoon_slots.count() / 2


@pytest.mark.django_db
def test_generate_delivery_slots_command_flags_special_delivery_item_slots_when_false():
    call_command("generate_delivery_slots")
    start_date = timezone.now().date()
    end_date = timezone.now().date() + timedelta(weeks=4)
    coming_wednesdays = list(filter(
        lambda day: WeekDays(day.weekday()).name == "wednesday",
        [start_date + timedelta(days=x) for x in range((end_date - start_date).days)],
    ))
    wednesday_slots = DeliverySlot.objects.filter(date__in=coming_wednesdays)
    for slot in wednesday_slots:
        assert slot.special_item is False
