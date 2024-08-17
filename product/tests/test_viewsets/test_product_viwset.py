import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from product.factories import ProductFactory, CategoryFactory
from product.models import Product
from rest_framework import status

class ProductViewSetTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(title="example product", price=100)
        self.product.category.set([self.category])
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        self.client.force_authenticate(user=None)

    def test_get_all_products(self):
        response = self.client.get(reverse("product-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)

        results = product_data  # Como já é uma lista
        self.assertTrue(len(results) > 0, "A lista de produtos está vazia.")
        if len(results) > 0:
            self.assertEqual(results[0]["title"], self.product.title)




