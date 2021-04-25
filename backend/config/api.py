from rest_framework import routers
from apps.users.views import UserViewSet
from apps.delivery_slots.views import DeliverySlotViewSet, UserDeliverySlotViewSet


# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)
api.register(r'slots', DeliverySlotViewSet, basename='slots')
api.register(r'user-slots', UserDeliverySlotViewSet, basename='user-slots')
