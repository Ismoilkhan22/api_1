from django.urls import path
from .views import Hisoblash

urlpatterns = [

    path('hisoblash/', Hisoblash.as_view())
]