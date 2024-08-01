from django.test import TestCase
from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer

class TestProductSerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title='technology')
        self.product_1 = ProductFactory(
            title='mouse', price=100.00, description='A computer mouse', active=True, category=[self.category]
        )
        self.product_serializer = ProductSerializer(self.product_1)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data['price'], '100.00')
        self.assertEqual(serializer_data['title'], 'mouse')
        self.assertEqual(serializer_data['description'], 'A computer mouse')
        self.assertEqual(serializer_data['active'], True)
        self.assertEqual(serializer_data['category'][0]['title'], 'technology')
