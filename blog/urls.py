from rest_framework.routers import DefaultRouter

from blog.views import ArticleModelViewSet

blog_router = DefaultRouter()

blog_router.register(r'articles', ArticleModelViewSet)

articles_urlpatterns = blog_router.urls