from django.test import TestCase
from product.factories import CategoryFactory
from product.serializers import CategorySerializer

class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title='food', slug='food-slug', description='Food category', active=True)
        self.category_serializer = CategorySerializer(self.category)

    def test_category_serializer(self):
        serializer_data = self.category_serializer.data
        self.assertEqual(serializer_data['title'], 'food')
        self.assertEqual(serializer_data['slug'], 'food-slug')
        self.assertEqual(serializer_data['description'], 'Food category')
        self.assertEqual(serializer_data['active'], True)

    
