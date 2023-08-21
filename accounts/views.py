from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class RegisterView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'status': 'User created successfully'})

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'status': 'Logged in successfully'})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
