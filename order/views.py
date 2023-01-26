from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework import status
from .serializers import OrderListSerializer
from .models import Order
from django.conf import settings

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
    
        
def order_detail_page_move(request):    
    return render(request, 'order_detail.html')   

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    
    serializer_class = OrderListSerializer
    # lookup_field = 'id'
    
    def get_queryset(self):
        return Order.objects.all().order_by('-id')
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)
