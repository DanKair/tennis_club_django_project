from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Player, PlayerManager
from .serializers import PlayerSerializer
from drf_spectacular.utils import extend_schema

# Create your views here.


#  @api_view(['GET', 'POST'])
#  def hello_world(request):
#      if request.method == 'POST':
#          return Response({"message": "Got some data!", "data": request.data})
#      return Response({"message": "Hello, world!"})

# CREATE Operation
# 1. Accept some data through request.data and serialize it
# 2. Validate the data
# 3. save it 
class CreatePlayerAPIView(APIView):
    @extend_schema(
    request=PlayerSerializer,
    responses=PlayerSerializer,
    description="Create a new player"
    )   
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Created Player": serializer.data})
        return Response(serializer.errors)
    

class ListPlayersAPIView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    
    
@api_view(["GET"])
def get_player_by_id(request, player_id): 
    player = get_object_or_404(Player, pk=player_id)
    serializer = PlayerSerializer(player)
    return Response({"player data": serializer.data})


class EditPlayerAPIView(APIView):
    """
    Edit Player By Player ID
    - You can partially change the data (No need to change all fields)
    - You can Delete the Player Objects By ID
    """
    def patch(self, request, player_id: int):
        player = get_object_or_404(Player, pk=player_id)
        serializer = PlayerSerializer(player, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, player_id):
        player = get_object_or_404(Player, pk=player_id)
        player.delete()
        return Response({"msg": f"Player with id {player_id} was deleted."}, status=status.HTTP_204_NO_CONTENT)
    


# @api_view(['PUT', 'DELETE'])
# def edit_players_by_id(request, player_id):
#     player = get_object_or_404(Player, pk=player_id)
#     if request.method == 'PUT':
#         serializer = PlayerSerializer(player, data=request.data)
#         if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#     return Response(serializer.errors)

#   elif request.method == "DELETE":
#       player_first_name = player.first_name
#       player.delete()
#       return Response("Deleted Player": player_first_name)

    