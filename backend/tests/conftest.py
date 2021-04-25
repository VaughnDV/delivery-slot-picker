from apps.delivery_slots.models import UserDeliverySlot
from apps.users.models import User


def add_user(first_name, email):
    user, created = User.objects.get_or_create(
        email=email,
        defaults=dict(first_name=first_name, last_name="")
    )
    return user


def add_user_delivery_booking(user_id, delivery_slot_id):
    return UserDeliverySlot.objects.create(user_id=user_id, delivery_slot_id=delivery_slot_id)
