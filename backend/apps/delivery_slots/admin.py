from django.contrib import admin
from .models import DeliverySlot, UserDeliverySlot


@admin.register(DeliverySlot)
class DeliverySlotAdmin(admin.ModelAdmin):
    list_display = ("date", "name",)
    search_fields = ("date", "name",)
    ordering = ["date"]


@admin.register(UserDeliverySlot)
class UserDeliverySlotAdmin(admin.ModelAdmin):
    list_display = ("user", "delivery_slot",)
    ordering = ["created_at"]
