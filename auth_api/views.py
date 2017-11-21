# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, views
from rest_framework.response import Response

from .serializers import UserSerializer
from django.shortcuts import render

# Create your views here.

class LoginView(views.APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password")
        )

        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username or Password Incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return  Response(UserSerializer(user).data)

class LogoutView(views.APIView):

    def  get(selfself, request):
        logout(request)
        return  Response({}, status=status.HTTP_204_NO_CONTENT)