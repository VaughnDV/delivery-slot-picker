from django.db import models
from apps.users.models import User
from .utils import WeekDays


class DeliverySlot(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    spaces = models.IntegerField(default=0)
    special_item = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def available(self):
        if UserDeliverySlot.objects.filter(delivery_slot=self.pk).count() < self.spaces:
            return True
        return False

    @property
    def day_of_the_week(self):
        return WeekDays(self.date.weekday()).name

    def check_availability(self):
        return self.available

    def __str__(self):
        return f"{self.date} {self.name}"


class UserDeliverySlot(models.Model):
    delivery_slot = models.ForeignKey(DeliverySlot, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.delivery_slot} {self.user}"
