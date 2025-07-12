from rest_framework.views import APIView
from authentication.serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUser(APIView):
    def gen_token(self, email, password):
        user = authenticate(username=email, password=password)
        refresh = RefreshToken.for_user(user)        
        return {
            'access' : str(refresh.access_token),
            'refresh' : str(refresh)
        }
    
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message' : "User Register Successfully", 
                'user' : serializer.data,
                'token' : self.gen_token(request.data.get("email"), 
                                         request.data.get("password"))}, 
                            status=status.HTTP_201_CREATED)
        return Response({'message' : serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)