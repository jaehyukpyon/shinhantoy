from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from .serializers import MemberRegisterSerializer
from .models import Member
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):    
    serializer_class = MemberRegisterSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

def login_page_move(request):
    return render(request, 'login.html')

class MemberIdDuplicateCheck(APIView):
    
    def post(self, request, *args, **kwargs):
        username = self.request.data['username']
        duplicate = Member.objects.filter(username=username).exists()
        response_data = { }
        if duplicate:
            response_data['result'] = True
        else:
            response_data['result'] = False
        return JsonResponse(response_data)
    
class MemberChangePasswordView(APIView):
    
    def put(self, request, *args, **kwargs):
        
        username = request.data.get('username')
        current = request.data.get('old_password')
        password1 = request.data.get('new_password1')
        password2 = request.data.get('new_password2')
        
        if password1 != password2:
            return Response({
                'detail': 'New password does not match.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if not Member.objects.filter(username=username).exists():
            return Response({
                'detail': 'No Account'
            }, status=status.HTTP_404_NOT_FOUND)
            
        member = Member.objects.get(username=username)
        
        if not check_password(current, member.password):
            return Response({
                'detail': 'Old and New password do not match'
            }, status=status.HTTP_400_BAD_REQUEST)
        member.password = make_password(password1)
        member.save()
        
        return Response({
            'detail': 'Successfully changed pw.'
        }, status=status.HTTP_201_CREATED)
        