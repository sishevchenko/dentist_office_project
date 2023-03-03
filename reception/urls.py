from django.urls import path
from . import views

urlpatterns = [
    path('receptions/', views.ReceptionAPIView.as_view()),
    path('receptions/<int:pk>/', views.ReceptionAPIView.as_view()),
]
