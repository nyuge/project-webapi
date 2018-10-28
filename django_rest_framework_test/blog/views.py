from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Entry, User
from .serializer import EntrySerializer, UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("author", "status")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
