from django.urls import include, path

auth_urlpatterns = [
    path('auth/', include('dj_rest_auth.registration.urls'))
]