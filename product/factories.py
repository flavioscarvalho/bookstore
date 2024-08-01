import factory
from product.models import Product, Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('word')
    slug = factory.Faker('slug')
    description = factory.Faker('text')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('word')
    description = factory.Faker('text')
    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    active = factory.Faker('boolean')

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)

    class Meta:
        model = Product
        skip_postgeneration_save = True  # Adicione esta linha

    @factory.post_generation
    def post(self, create, extracted, **kwargs):
        if create:
            self.save()




