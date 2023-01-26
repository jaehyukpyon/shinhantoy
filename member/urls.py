from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MemberRegisterView.as_view()),
    path('move/', views.login_page_move),    
    path('duplicate/', views.MemberIdDuplicateCheck.as_view()),
    path('password/', views.MemberChangePasswordView.as_view()),
    path('api/order/', include('order.urls')),
]
