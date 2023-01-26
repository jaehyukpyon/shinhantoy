from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework import status
from .serializers import OrderListSerializer, CommentSerializer
from .models import Order, Comment
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

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
    

class CommentWriteView(
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    permission_classes = [IsAuthenticated]
    
    serializer_class = CommentSerializer
    
    def post(self, request, *args, **kwargs):
        print('##### request.data > ', request.data)
        # data = {}
        # for key, value in request.data.lists():
        #     print(f'@@@@@ key: {key}, value: {value[0].strip()}')
        #     data[key] = value[0].strip()
        
        # data['member'] = request.user.id
        # print(f'$$$$$ data > {data}')
        # request.data = data
        return self.create(request, args, kwargs)
    
class CommentCreateListView(
    mixins.CreateModelMixin, 
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Comment.objects.filter(order_id=self.kwargs['order_id'])
    
    serializer_class = CommentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        print('##### request.data > ', request.data)
        # data = {}
        # for key, value in request.data.lists():
        #     print(f'@@@@@ key: {key}, value: {value[0].strip()}')
        #     data[key] = value[0].strip()
        
        # data['member'] = request.user.id
        # print(f'$$$$$ data > {data}')
        # request.data = data
        return self.create(request, args, kwargs)
    
class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.filter(order_id=self.kwargs['order_id'])
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
