from django.test import TestCase
from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer

class TestOrderSerializer(TestCase):
    def setUp(self):
        self.product_1 = ProductFactory(price=10)
        self.product_2 = ProductFactory(price=20)
        self.order = OrderFactory(product=[self.product_1, self.product_2])
        self.order_serializer = OrderSerializer(instance=self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data
        self.assertEqual(serializer_data['product'][0]['title'], self.product_1.title)
        self.assertEqual(serializer_data['product'][1]['title'], self.product_2.title)
        self.assertEqual(serializer_data['total'], 30)  # Verificando o campo total

