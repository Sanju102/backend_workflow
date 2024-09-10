from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from user.api.views import logout_user,register_user,user_list

urlpatterns = [
    path('login/', ObtainAuthToken.as_view(), name='login-token' ),
    path('logout/', logout_user, name='logout-token' ),
    path('register/', register_user, name='register' ),
    path('list/', user_list, name='user-list' ),
]