import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from product.factories import CategoryFactory
from product.models import Category

class CategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="books")
        self.update_url = reverse('update')
        self.hello_world_url = reverse('hello_world')

    def test_get_all_category(self):
        response = self.client.get(
            reverse("category-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)

        self.assertEqual(category_data[0]["title"], self.category.title)

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
        self.assertJSONEqual(response.content.decode('utf8'), {"status": "update successful"})

    def test_hello_world_view(self):
        response = self.client.get(self.hello_world_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content.decode('utf8'), {"message": "Hello, world!"})
