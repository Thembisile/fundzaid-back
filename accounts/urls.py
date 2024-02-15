from django.urls import path
from .views import LoginView, RegisterView, UserProfileListCreateView, UserProfileRetrieveUpdateDestroyView


urlpatterns = [
    path('login/', LoginView.as_view(), name='api_login'),
    path('register/', RegisterView.as_view(), name='api_register'),
    path('profiles/', UserProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDestroyView.as_view(), name='profile-retrieve-update-destroy'),
]
