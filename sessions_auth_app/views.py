import json

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers, generics


class LoginSerializer(serializers.Serializer):
    username = CharField()
    password = CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not username and password:
            raise ValidationError(detail='You should provide username and password.')

        return super(LoginSerializer, self).validate(attrs)


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        user = authenticate(username=data.get('username'), password=data.get('password'))

        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response(status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def logout(request):
    if request.user.is_authenticated:
        return Response(data={'detail': "You are not logged in."}, status=status.HTTP_401_UNAUTHORIZED)

    logout(request)

    return Response(data={'detail': "You are logged out."}, status=status.HTTP_200_OK)


# class LogoutView(GenericAPIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return Response(data={'detail': "You are not logged in."}, status=status.HTTP_401_UNAUTHORIZED)
#
#         logout(request)
#
#         return Response(data={'detail': "You are logged out."}, status=status.HTTP_200_OK)
