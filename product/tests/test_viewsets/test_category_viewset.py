import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from product.factories import CategoryFactory
from rest_framework import status

class CategoryViewSetTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="books")
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        self.client.force_authenticate(user=None)

    def test_get_all_category(self):
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)

        results = category_data  # Como já é uma lista
        self.assertTrue(len(results) > 0, "A lista de categorias está vazia.")
        if len(results) > 0:
            self.assertEqual(results[0]["title"], self.category.title)
