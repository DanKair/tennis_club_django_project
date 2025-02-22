from rest_framework import serializers
from .models import Player, PlayerManager
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_first_name', 'player_last_name', 'player_email', 'player_age', 'matches_played']
