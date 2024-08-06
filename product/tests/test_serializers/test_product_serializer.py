import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from product.factories import ProductFactory, CategoryFactory
from product.models import Product


class TestProductSerializer(APITestCase):
    client = APIClient()

    def setUp(self) -> None:
        self.category = CategoryFactory(title="technology")
        self.product_1 = ProductFactory(title="mouse", price=100)
        self.product_1.category.set([self.category])  # Use .set() instead of direct assignment

    def test_product_serializer(self):
        data = {
            "title": "new product",
            "description": "This is a new product",
            "price": "9.99",
            "active": True,
            "categories_id": [self.category.id]
        }

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=json.dumps(data),
            content_type="application/json",
        )

        print("Status Code:", response.status_code)
        print("Response Content:", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
