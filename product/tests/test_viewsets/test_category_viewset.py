import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from django.contrib.auth.models import User

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="books")
        self.update_url = reverse("update")
        self.hello_world_url = reverse("hello_world")
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)  # Autenticação

    def tearDown(self):
        self.client.force_authenticate(user=None)  # Remove a autenticação após os testes

    def test_get_all_category(self):
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)

        # Verifique se o retorno é uma lista
        if isinstance(category_data, list):
            results = category_data
        else:
            # Se não for uma lista, tenta acessar 'results' como chave do dicionário
            results = category_data.get("results", [])

        # Verifique se a lista de resultados não está vazia
        self.assertTrue(len(results) > 0, "A lista de categorias está vazia.")
        if len(results) > 0:
            self.assertEqual(results[0]["title"], self.category.title)

    def test_create_category(self):
        data = json.dumps({"title": "technology", "slug": "technology"})

        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_category = Category.objects.get(title="technology")

        self.assertEqual(created_category.title, "technology")
        self.assertEqual(created_category.slug, "technology")

    def test_update_view(self):
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            response.content.decode("utf8"), {"status": "update successful"}
        )

    def test_hello_world_view(self):
        response = self.client.get(self.hello_world_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            response.content.decode("utf8"), {"message": "Hello, world!"}
        )
