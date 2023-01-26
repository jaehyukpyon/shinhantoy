from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from .serializers import MemberRegisterSerializer
from .models import Member
from django.http import JsonResponse

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
