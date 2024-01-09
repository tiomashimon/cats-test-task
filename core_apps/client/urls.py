from django.urls import path
from .views import signup, signin, home, profile, about, verification

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('about/', about, name='about'),
    path('verification/', verification, name='verification'),
]
