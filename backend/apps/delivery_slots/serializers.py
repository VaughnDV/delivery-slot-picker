from rest_framework import serializers
from .models import DeliverySlot, UserDeliverySlot


class DeliverySlotSerializer(serializers.ModelSerializer):
    available = serializers.SerializerMethodField(read_only=True)

    def get_available(self, obj):
        return obj.available

    class Meta:
        model = DeliverySlot
        fields = ["id", "name", "date", "start_time", "end_time", "special_item", "available"]


class UserDeliverySlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDeliverySlot
        fields = ["id", "delivery_slot"]
