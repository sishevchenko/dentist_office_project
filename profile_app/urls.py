from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserAPIView.as_view()),
    path('users/<int:pk>/', views.UserAPIView.as_view()),
    path('groups/', views.GroupAPIView.as_view()),
    path('groups/<int:pk>/', views.GroupAPIView.as_view()),
]
