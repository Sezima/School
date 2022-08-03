
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Successfully signed up!", status=status.HTTP_201_CREATED)
        return Response('Not valid', status=status.HTTP_400_BAD_REQUEST)




class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

class LogoutView(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Successfully logout', status=status.HTTP_200_OK)
