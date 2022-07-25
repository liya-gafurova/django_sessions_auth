from blog.models import Article


def get_users_articles(user):
    return Article.objects.filter(author=user)