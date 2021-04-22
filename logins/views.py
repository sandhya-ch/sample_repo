from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import login, authenticate


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]

    def post(self, request, *args, **kwargs):
        data = request.data
        print("sandhyaaaaaaaaaaaaaaaaaaaaaa")
        print(data)
        data['username'] = data.get('username')
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })

class LoginView(generics.RetrieveAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message":"login successfully"}, status=status.HTTP_200_OK)
        return Response({"message":"user details not found"}, status=status.HTTP_401_UNAUTHORIZED)