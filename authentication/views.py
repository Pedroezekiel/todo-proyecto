from rest_framework import viewsets
from .models import AppUser


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()

