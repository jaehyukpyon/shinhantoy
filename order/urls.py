from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view()),
    #path('move', views.order_detail_page_move),
    path('<int:pk>', views.OrderDetailView.as_view()),
    path('comment', views.CommentCreateView.as_view()),
    path('<int:order_id>/comments', views.CommentListView.as_view()),
    path('comment/<int:pk>', views.CommentDeleteView.as_view()),
    path('<int:pk>/likes', views.LikeCountView.as_view()),
]