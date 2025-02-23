from rest_framework import serializers
from .models import Player, PlayerManager
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'email', 'age', 'matches_played']
