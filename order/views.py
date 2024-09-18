from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        products_id = data.get("products_id")
        products = Product.objects.filter(id__in=products_id)
        order = Order.objects.create(user=user)
        order.product.set(products)
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)
