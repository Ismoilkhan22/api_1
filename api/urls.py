from django.urls import path
from .views import TelefonVeiw

urlpatterns = [

    path('', TelefonVeiw.as_view()),
    path('<int:pk>/', TelefonVeiw.as_view()),
]