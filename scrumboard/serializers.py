from rest_framework import serializers

from .models import Board, Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True)
    class Meta:
        model = Board
        fields = ('__all__')




