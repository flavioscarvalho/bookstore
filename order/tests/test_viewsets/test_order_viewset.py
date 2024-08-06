import json
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from product.factories import ProductFactory, CategoryFactory
from order.models import Order
from order.factories import OrderFactory


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(title="mouse", price=100)
        self.product.category.set([self.category])  # Use .set() instead of direct assignment
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_create_order(self):
        data = {
            "user": self.user.id,
            "products_id": [self.product.id],
            "quantity": 1
        }

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=json.dumps(data),
            content_type="application/json",
        )

        print("Status Code:", response.status_code)
        print("Response Content:", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_order(self):
        data = {
            "user": self.user.id,
            "products_id": [self.product.id],
            "quantity": 1
        }

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=json.dumps(data),
            content_type="application/json",
        )

        print("Status Code:", response.status_code)
        print("Response Content:", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
