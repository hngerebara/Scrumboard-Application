# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from .serializers import BoardSerializer,  CardSerializer
# from .models import Board, Card
# from rest_framework.views import APIView
# from rest_framework.viewsets import  ModelViewSet
# from rest_framework.response import Response
# from rest_framework import status
#
#
# # Create your views here.
# class BoardViewSet(APIView):
#     """
#        List all Boards, or create a new board, update a board and delete a board.
#        """
#     def get(self, request, format=None):
#         boards = Board.objects.all()
#         serializer = BoardSerializer(boards, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = BoardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, format=None):
#         board = self.get_object(pk)
#         serializer = BoardSerializer(board, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         board = self.get_object(pk)
#         board.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
# class CardViewSet(APIView):
#     """
#        List all cards, or create a new card, update a card and delete a card.
#        """
#
#     def get(self, request, format=None):
#         cards =Card.objects.all()
#         serializer = CardSerializer(cards, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, format=None):
#         card = self.get_object(pk)
#         serializer = CardSerializer(card, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         card = self.get_object(pk)
#         card.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .serializers import BoardSerializer,  CardSerializer
from .models import Board, Card
from rest_framework.viewsets import  ModelViewSet


# Create your views here.
class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer




class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
