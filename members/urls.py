from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPlayersAPIView.as_view(), name="Players List Fetch"),
]