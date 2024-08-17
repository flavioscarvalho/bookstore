# import json
# from django.urls import reverse
# from rest_framework.test import APIClient, APITestCase
# from rest_framework.views import status

# from product.factories import ProductFactory, CategoryFactory
# from product.models import Product


# class TestProductSerializer(APITestCase):
#     client = APIClient()

#     def setUp(self) -> None:
#         self.category = CategoryFactory(title="technology")
#         self.product_1 = ProductFactory(title="mouse", price=100)
#         self.product_1.category.set([self.category])  # Use .set() instead of direct assignment

#     def test_product_serializer(self):
#         data = {
#             "title": "new product",
#             "description": "This is a new product",
#             "price": "9.99",
#             "active": True,
#             "categories_id": [self.category.id]
#         }

#         response = self.client.post(
#             reverse("product-list", kwargs={"version": "v1"}),
#             data=json.dumps(data),
#             content_type="application/json",
#         )

#         print("Status Code:", response.status_code)
#         print("Response Content:", response.content)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


import json
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from django.contrib.auth.models import User


from product.factories import ProductFactory, CategoryFactory
from product.models import Product


class ProductViewSetTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(title="example product", price=100)
        self.product.category.set([self.category])
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)  # Autenticação

    def tearDown(self):
        self.client.force_authenticate(
            user=None
        )  # Remove a autenticação após os testes

    # def test_get_all_products(self):
    #     response = self.client.get(
    #         reverse("product-list", kwargs={"version": "v1"}))

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     product_data = json.loads(response.content)

    #     self.assertTrue(len(product_data) > 0, "A lista de produtos está vazia.")
    #     self.assertEqual(product_data[0]["title"], self.product.title)

    def test_get_all_products(self):
        response = self.client.get(reverse("product-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)

        # Log para verificar o conteúdo de product_data
        print("Product Data:", product_data)

        # Acessando a lista de resultados corretamente
        results = product_data.get("results", [])

        self.assertTrue(len(results) > 0, "A lista de produtos está vazia.")
        if len(results) > 0:
            self.assertEqual(results[0]["title"], self.product.title)

    def test_create_product(self):
        data = {
            "title": "new product",
            "description": "This is a new product",
            "price": "9.99",
            "active": True,
            "slug": "new-product",
            "categories_id": [self.category.id],
        }

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=json.dumps(data),
            content_type="application/json",
        )

        print("Status Code:", response.status_code)
        print("Response Content:", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
