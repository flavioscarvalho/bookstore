from django.test import TestCase
from product.factories import CategoryFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        # Cria uma instância de Category para ser usada nos testes
        self.category = CategoryFactory(title="food")
        # Cria uma instância do serializer usando a categoria criada
        self.category_serializer = CategorySerializer(self.category)

    def test_category_serializer(self):
        # Serializa os dados da categoria
        serializer_data = self.category_serializer.data

        # Verifica se o campo 'title' está correto
        self.assertEqual(serializer_data["title"], "food")
