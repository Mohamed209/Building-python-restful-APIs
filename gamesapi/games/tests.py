from django.test import TestCase
# Create your tests here.
from datetime import datetime
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from games.models import Game
from games.serializers import GameSerializer
from io import BytesIO


gamedatetime = timezone.make_aware(
    datetime.now(), timezone.get_current_timezone())
game1 = Game(name='Smurfs Jungle', release_date=gamedatetime,
             game_category='2D mobile arcade', played=False)
game1.save()
game2 = Game(name='Angry Birds RPG', release_date=gamedatetime,
             game_category='3D RPG', played=False)
game2.save()

print(game1.pk)
print(game1.name)
print(game1.created)
print(game2.pk)
print(game2.name)
print(game2.created)

gameser1 = GameSerializer(game1)
print("serializer data of game1 >>> \n", gameser1.data)
gameser2 = GameSerializer(game2)
print("serializer data of game2 >>> \n", gameser2.data)

renderer = JSONRenderer()
datagame1 = renderer.render(gameser1.data)
print("rendered game1 data >>> \n", datagame1)

json_string_for_new_game = '{"name":"Tomb Raider Extreme Edition","release_date":"2016-05-18T03:02:00.776594Z","game_category":"3D RPG","played":false}'
json_bytes_for_new_game = bytes(json_string_for_new_game, encoding="UTF-8")
stream_for_new_game = BytesIO(json_bytes_for_new_game)
parser = JSONParser()
parsed_new_game = parser.parse(stream_for_new_game)
print("new game >>> \n", parsed_new_game)

new_game_serializer = GameSerializer(data=parsed_new_game)
if new_game_serializer.is_valid():
    new_game = new_game_serializer.save()
    print("added new game >>> \n", new_game.name)

