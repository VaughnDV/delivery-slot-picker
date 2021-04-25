from rest_framework.permissions import IsAuthenticated
from .models import DeliverySlot, UserDeliverySlot
from .serializers import UserDeliverySlotSerializer, DeliverySlotSerializer
from rest_framework import mixins
from rest_framework import viewsets


class DeliverySlotViewSet(
    viewsets.ReadOnlyModelViewSet,
):
    """
    A read only paginated viewset that provides `list` action on delivery slots.
    """

    queryset = DeliverySlot.objects.all()
    serializer_class = DeliverySlotSerializer
    permission_classes = []


class UserDeliverySlotViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    A viewset that provides `create` and `list` actions on the user's delivery slots.
    """

    queryset = UserDeliverySlot.objects.all()
    serializer_class = UserDeliverySlotSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        delivery_slot = DeliverySlot.objects.get(id=self.request.data.get('delivery_slot'))
        if delivery_slot.check_availability() is True:
            serializer.save(user=self.request.user, delivery_slot=delivery_slot)
