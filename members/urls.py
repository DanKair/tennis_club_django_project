from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPlayersAPIView.as_view(), name="Players List Fetch"),
    path('create/', views.CreatePlayerAPIView.as_view(), name="Player Create View"),
    path('<int:player_id>', views.get_player_by_id, name="Get Player by Player ID"),
    path('edit/<int:player_id>', views.EditPlayerAPIView.as_view(), name="Delete and Update Players"),
]