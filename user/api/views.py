from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

@api_view(['GET'])
def user_list(request):
    if request.method=='GET':
        user=User.objects.all()
        data=UserSerializer(user,many=True)
        return Response(data.data)

@api_view(['POST'])
def logout_user(request):
    if request.method=='POST':
        username=request.user.username
        print(username)
        user=User.objects.get(username=username) 
        token=Token.objects.filter(user=user)
        token.delete()
        return Response({"message":"Log out succesfully"})
    
@api_view(['POST'])
def register_user(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User has been created"})