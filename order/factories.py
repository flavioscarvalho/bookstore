# import factory
# from factory.django import DjangoModelFactory
# from order.models import Order
# from product.factories import ProductFactory
# from django.contrib.auth.models import User

# class OrderFactory(DjangoModelFactory):
#     class Meta:
#         model = Order
#         skip_postgeneration_save = True

#     user = factory.SubFactory(factory.django.DjangoModelFactory, model=User)

#     @factory.post_generation
#     def products(self, create, extracted, **kwargs):
#         if not create:
#             return
#         if extracted:
#             for product in extracted:
#                 self.product.add(product)

import factory
from factory.django import DjangoModelFactory
from order.models import Order
from product.factories import ProductFactory
from django.contrib.auth.models import User


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order
        skip_postgeneration_save = True  # Adicionando esta linha para resolver o aviso

    user = factory.SubFactory(factory.django.DjangoModelFactory, model=User)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for product in extracted:
                self.product.add(product)
        self.save()  # Salvando a instância após adicionar os produtos
