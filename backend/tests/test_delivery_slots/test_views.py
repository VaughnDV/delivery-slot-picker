import json

import pytest
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.test import force_authenticate
from apps.delivery_slots.models import DeliverySlot
from apps.delivery_slots.views import UserDeliverySlotViewSet
from tests.conftest import add_user, add_user_delivery_booking
from django.core.management import call_command


@pytest.mark.django_db
def test_get_delivery_slot_list():
    call_command("generate_delivery_slots")

    client = APIClient()
    response = client.get("/api/slots")

    assert response.status_code == 200


@pytest.mark.django_db
def test_get_delivery_slot_is_marked_not_available():
    call_command("generate_delivery_slots")
    user = add_user(first_name="test", email="test@gmail.com")
    delivery_slot = DeliverySlot.objects.first()
    for i in range(5):
        add_user_delivery_booking(user.id, delivery_slot.id)

    client = APIClient()
    response = client.get("/api/slots")
    response_slot = json.loads(response.content)["results"][0]

    assert response_slot["id"] == delivery_slot.id
    assert response_slot["available"] is False


@pytest.mark.django_db
def test_get_lists_user_delivery_slot():
    call_command("generate_delivery_slots")
    user = add_user(first_name="test", email="test@gmail.com")
    delivery_slot = DeliverySlot.objects.first()
    add_user_delivery_booking(user.id, delivery_slot.id)

    factory = APIRequestFactory()
    view = UserDeliverySlotViewSet.as_view({'get': 'list'})
    request = factory.get("/api/user-slots")
    force_authenticate(request, user=user)
    response = view(request)
    response_slot = json.loads(response.rendered_content)["results"][0]["delivery_slot"]

    assert response_slot == delivery_slot.id
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_creates_user_delivery_slot():
    call_command("generate_delivery_slots")
    user = add_user(first_name="test", email="test@gmail.com")
    delivery_slot = DeliverySlot.objects.first()
    add_user_delivery_booking(user.id, delivery_slot.id)

    factory = APIRequestFactory()
    view = UserDeliverySlotViewSet.as_view({'post': 'create'})
    request = factory.post(
        "/api/user-slots",
        data={
            "delivery_slot": delivery_slot.id
        }
    )
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == 201
