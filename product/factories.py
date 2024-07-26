import factory
from product.models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('word')
    description = factory.Faker('text')
    price = factory.Faker('random_number', digits=4)
    active = True

    class Meta:
        model = Product
        skip_postgeneration_save = True  # Adicione esta linha

    @factory.post_generation
    def post(self, create, extracted, **kwargs):
        if create:
            self.save()

