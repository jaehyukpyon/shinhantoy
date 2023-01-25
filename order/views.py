from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework import status
from .serializers import OrderListSerializer
from .models import Order

# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = OrderListSerializer
    
    def get_queryset(self):
        return Order.objects.all().order_by('-id')
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
