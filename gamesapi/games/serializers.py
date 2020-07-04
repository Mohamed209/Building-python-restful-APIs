from rest_framework import serializers
from games.models import Game

# check : https://www.django-rest-framework.org/api-guide/serializers/#modelserializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id',
                  'name',
                  'release_date',
                  'game_category',
                  'played']
