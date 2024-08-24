import factory
from factory.django import DjangoModelFactory
from product.models import Product, Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Faker("word")
    description = factory.Faker("text")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product
        skip_postgeneration_save = True  

    title = factory.Faker("word")
    description = factory.Faker("text")
    price = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    active = factory.Faker("boolean")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.category.add(category)
        self.save() 
