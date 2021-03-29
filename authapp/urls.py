from django.urls import path
from authapp.views import logout, GeekLoginView, RegisterView, ProfileView

app_name = 'authapp'

urlpatterns = [
    path('login/', GeekLoginView, name='login'),
    path('register/', RegisterView, name='register'),
    path('logout', logout, name='logout'),
    path('profile', ProfileView, name='profile'),
    path('verify/<str:email>/<str:activation_key>/', RegisterView.verify, name='verify'),
]
