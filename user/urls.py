# urls.py
from django.urls import path
from .views import login , dummy , register
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('login/', login),
    path('register/',register),
    path('check/' , dummy)
    # path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/refresh/' , TokenRefreshView.as_view() , name='refersh')
]