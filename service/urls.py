from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.ServiceAPIView.as_view()),
    path('services/<int:pk>/', views.ServiceAPIView.as_view()),
]
