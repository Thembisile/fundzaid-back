from rest_framework import serializers
from .models import Campaign, Fundraiser

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class FundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraiser
        fields = '__all__'
