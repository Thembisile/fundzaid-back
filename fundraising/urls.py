from django.urls import path, include
from .views import CampaignViewSet, FundraiserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'fundraisers', FundraiserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
