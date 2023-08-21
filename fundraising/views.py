from rest_framework import viewsets
from .models import Campaign, Fundraiser
from .serializers import CampaignSerializer, FundraiserSerializer
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class FundraiserViewSet(viewsets.ModelViewSet):
    queryset = Fundraiser.objects.all()
    serializer_class = FundraiserSerializer


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Logged in successfully")
        else:
            return HttpResponse("Invalid credentials")
    else:
        # Render login form
        ...

def user_register(request):
    if request.method == 'POST':
        # Handle user registration logic
        ...
    else:
        # Render registration form
        ...
