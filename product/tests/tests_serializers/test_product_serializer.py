from rest_framework.test import APITestCase
from product.serializers import ProductSerializer
from product.models import Product, Category

class TestProductSerializer(APITestCase):
    
    def setUp(self):
        # Criando instâncias de Category usando o campo 'title' em vez de 'name'
        self.category1 = Category.objects.create(title="Electronics", slug="electronics")
        self.category2 = Category.objects.create(title="Books", slug="books")
        
        # Dados de exemplo para o teste
        self.product_data = {
            "title": "Laptop",
            "description": "A high-end gaming laptop",
            "price": 2500,
            "active": True,
        }
        # Cria uma instância de Product e adiciona categorias
        self.product = Product.objects.create(**self.product_data)
        self.product.category.set([self.category1, self.category2])
        self.product.save()
        
        # Inicializa o serializer com a instância criada
        self.product_serializer = ProductSerializer(instance=self.product)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data['title'], 'Laptop')
        self.assertEqual(serializer_data['description'], 'A high-end gaming laptop')
        self.assertEqual(serializer_data['price'], 2500)
        self.assertEqual(serializer_data['active'], True)
        self.assertEqual(len(serializer_data['category']), 2)  # Verifica se existem 2 categorias
