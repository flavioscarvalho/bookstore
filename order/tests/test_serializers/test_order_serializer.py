import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from product.factories import ProductFactory
from order.factories import OrderFactory
from django.contrib.auth.models import User


class TestOrderSerializer(APITestCase):
    client = APIClient()

    def setUp(self) -> None:
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()

        self.user = User.objects.create_user(username="testuser", password="12345")
        self.order = OrderFactory(
            user=self.user, products=[self.product_1, self.product_2]
        )
        self.client.login(username="testuser", password="12345")

    def test_order_serializer(self):
        data = {
            "user": self.user.id,
            "products_id": [self.product_1.id],
        }

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=json.dumps(data),
            content_type="application/json",
        )

        print("Status Code:", response.status_code)
        print("Response Content:", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
