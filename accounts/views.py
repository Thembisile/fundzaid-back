from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.generics import CreateAPIView
from .serializers import LoginSerializer
from rest_framework.renderers import TemplateHTMLRenderer
import logging

logger = logging.getLogger(__name__)




class UserProfileCreateView(CreateAPIView):
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class RegisterView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
    # Check if the username already exists
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')

        user = User.objects.create_user(username=username, password=password, email=email)
    
        return Response({'status': 'User created successfully'})
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            logger.debug(f"Attempting to authenticate user {username}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                logger.debug(f"User {username} authenticated")
                login(request, user)
                response_data = {'status': 'Logged in successfully'}
            else:
                logger.debug(f"Authentication failed for user {username}")
                response_data = {'error': 'Invalid credentials'}
                return Response(response_data, status=400)
            return Response(response_data)
        else:
            logger.debug(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=400)
