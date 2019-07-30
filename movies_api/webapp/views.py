from django.shortcuts import render
from webapp.permissions import IsOwnerOrReadOnly
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, permissions, filters
from webapp.models import movie
from webapp.serializers import movieSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly]


class movieList(viewsets.ModelViewSet):

    queryset = movie.objects.all()
    serializer_class = movieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'year']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

