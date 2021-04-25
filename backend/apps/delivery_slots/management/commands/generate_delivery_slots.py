from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import timedelta

from apps.delivery_slots.models import DeliverySlot
from apps.delivery_slots.config import (
    GENERATED_WEEKS,
    SLOTS_CONFIG,
    DEFAULT_NUMBER_OF_SLOTS,
    DEFAULT_FREQUENCY,
    DEFAULT_SPECIAL_ITEMS,
)
from apps.delivery_slots.utils import WeekDays, is_alternate_week


class Command(BaseCommand):
    help = f"Generates slots for the next {GENERATED_WEEKS} weeks if they do not already exist"

    def handle(self, *args, **options):

        try:
            st = timezone.now()
            self.stdout.write(f"Generating slots started at: {str(st)}")
            start_date = timezone.now().date()
            end_date = timezone.now().date() + timedelta(weeks=GENERATED_WEEKS)

            list_of_dates = [
                start_date + timedelta(days=x)
                for x in range((end_date - start_date).days)
            ]

            for this_date in list_of_dates:
                day_of_the_week = WeekDays(this_date.weekday()).name
                for slot in SLOTS_CONFIG:
                    if slot[day_of_the_week].get(
                        "frequency", DEFAULT_FREQUENCY
                    ) == "fortnight" and is_alternate_week(start_date, this_date):
                        continue

                    defaults = dict(
                        start_time=slot["start_time"],
                        end_time=slot["end_time"],
                        spaces=slot[day_of_the_week].get(
                            "number_of_slots", DEFAULT_NUMBER_OF_SLOTS
                        ),
                        special_item=slot[day_of_the_week].get(
                            "special_item", DEFAULT_SPECIAL_ITEMS
                        ),
                    )

                    DeliverySlot.objects.update_or_create(
                        name=slot["name"],
                        date=this_date,
                        defaults={k: v for k, v in defaults.items()},
                    )

            self.stdout.write(f"List of dates at: {str(list_of_dates)}")

            et = timezone.now()
            self.stdout.write(f"Generating slots ended successfully at: {str(et)}")

        except Exception as e:
            self.stdout.write(e)
            raise CommandError("Failed to generating slots")
