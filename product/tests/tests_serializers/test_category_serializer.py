from rest_framework.test import APITestCase
from product.serializers import CategorySerializer
from product.models import Category

class TestCategorySerializer(APITestCase):
    
    def setUp(self):
        # Dados de exemplo para o teste
        self.category_data = {
            "title": "food",
            "description": "All kinds of food"
        }
        # Cria uma instância de Category com os dados de exemplo
        self.category = Category.objects.create(**self.category_data)
        # Inicializa o serializer com a instância criada
        self.category_serializer = CategorySerializer(instance=self.category)

    def test_category_serializer(self):
        # Obtém os dados serializados
        serializer_data = self.category_serializer.data
        # Verifica se os dados serializados correspondem aos dados esperados
        self.assertEqual(serializer_data['title'], 'food')
        self.assertEqual(serializer_data['description'], 'All kinds of food')

