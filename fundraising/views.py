from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as django_filters
from .models import Campaign, Fundraiser
from .serializers import CampaignSerializer, FundraiserSerializer
from django.contrib.auth.models import User

class CampaignFilter(django_filters.FilterSet):
    min_goal = django_filters.NumberFilter(field_name="goal", lookup_expr='gte')
    max_goal = django_filters.NumberFilter(field_name="goal", lookup_expr='lte')

    class Meta:
        model = Campaign
        fields = ['min_goal', 'max_goal']

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = CampaignFilter
    ordering_fields = ['goal', 'title']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['GET'])
    def fundraisers(self, request, pk=None):
        campaign = self.get_object()
        fundraisers = Fundraiser.objects.filter(campaign=campaign)
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)

class FundraiserViewSet(viewsets.ModelViewSet):
    queryset = Fundraiser.objects.all()
    serializer_class = FundraiserSerializer

    def perform_create(self, serializer):
        serializer.save(donated_by=self.request.user)
