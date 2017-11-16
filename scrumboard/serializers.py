from rest_framework import serializers

from .models import Board, Card


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ('id','name')


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

