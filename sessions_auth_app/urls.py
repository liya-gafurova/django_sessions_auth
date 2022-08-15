from django.urls import include, path, re_path

from sessions_auth_app.views import *

auth_urlpatterns = [
    path('auth/', include('dj_rest_auth.registration.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='login')
]