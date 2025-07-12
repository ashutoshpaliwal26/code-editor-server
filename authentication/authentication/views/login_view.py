from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from authentication.serializer import RegisterSerializer
from authentication.models import CustomUser

class LoginView(APIView):
    def get_user(self, email):
        try:
            user = CustomUser.objects.get(email=email)
            serializer = RegisterSerializer(user)
            return serializer.data
        except:
            raise Exception("User Not Found")
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = authenticate(username=email, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message' : "Login Successfull",
                    'user' : self.get_user(email),
                    'token' : {
                    'refresh' : str(refresh),
                    'access' : str(refresh.access_token)
                }}, status=status.HTTP_200_OK)
            return Response({'message' : "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)