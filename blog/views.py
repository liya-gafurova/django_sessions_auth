from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from blog.dml import get_users_articles
from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleModelViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    @action(detail=False, methods=['get', ])
    def my_articles(self, request):
        users_articles = get_users_articles(request.user)

        return Response(users_articles)

    def create(self, request, *args, **kwargs):
        article = request.data
        article['user'] = request.user
        serializer = self.get_serializer(data=article)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# TODO https://github.com/duplxey/django-spa-cookie-auth/blob/master/django_react_same_origin/backend/api/views.py