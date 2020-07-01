from django.shortcuts import render
from games.models import Game
from games.serializers import GameSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
# Create your views here.


@csrf_exempt
def fetch_all_games(request):
    """
    fetches all games from  db
    """
    if request.method == 'GET':
        games = Game.objects.all()
        seria = GameSerializer(games, many=True)
        return JsonResponse(seria.data, safe=False)
    elif request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse(game_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def game_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return JsonResponse(game_serializer.data)

    elif request.method == 'PUT':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(game, data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()  # will update existing record with corresponding pk
            return JsonResponse(game_serializer.data)
        return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        game.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
