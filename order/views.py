from django.shortcuts import render
from django.conf import settings
from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import OrderListSerializer, CommentSerializer
from .models import Order, Comment, Like

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
    """
    이 함수는 order_list 페이지에서 한 개의 주문을 클릭 시 상세 페이지로 이동하도록 구현하기 위해 작성했습니다.
    단순하게 html 페이지를 보여주는 용도입니다.
    """  
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
   
# data = {}
# for key, value in request.data.lists():
#     print(f'@@@@@ key: {key}, value: {value[0].strip()}')
#     data[key] = value[0].strip()

# data['member'] = request.user.id
# print(f'$$$$$ data > {data}')
# request.data = data
    
class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    
    permission_classes = [IsAuthenticated]    
    serializer_class = CommentSerializer
    
    def post(self, request, *args, **kwargs):
        print('##### request.data > ', request.data)
        return self.create(request, args, kwargs)
    
class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.filter(order_id=self.kwargs['order_id']).order_by('-id')
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
class CommentDeleteView(
    mixins.DestroyModelMixin, 
    generics.GenericAPIView,
):
    
    permission_classes = [IsAuthenticated] 
    queryset = Comment.objects.all()
    
    def delete(self, request, *args, **kwargs):
        comment = Comment.objects.get(id=self.kwargs['pk'])
        
        if not comment:
            return Response({
                'detail': 'Comment does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if comment.member.username != request.user.username:
            print('작성자가 아님!!!!!!!!!!!!')
            return Response({
                'detail': 'Not Writer of This Comment.'
            }, status=status.HTTP_400_BAD_REQUEST)        
        elif comment.member.username == request.user.username:
            return self.destroy(request, args, kwargs)
        else:     
            return Response({
                'detail': 'Internal Error!'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class LikeCountView(
    APIView
):
    
    def get(self, request, pk):
        pk = self.kwargs['pk']
        queryset = Comment.objects.filter(order_id=pk)
        print('queryset > ', queryset)
        
        comment_id_list = []
        
        if not queryset:
            print('!@#$%^&*()')
            
        if queryset:
            queryset_list = list(queryset)
            print('##### queryset_list > ', queryset_list)
            for item in queryset_list:                
                comment_id_list.append(item.id)
        print(f'comment_id_list > {comment_id_list}')
        return Response({}, status=status.HTTP_200_OK)
            
