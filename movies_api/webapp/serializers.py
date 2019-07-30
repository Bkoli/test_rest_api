from django.contrib.auth.models import User
from rest_framework import serializers
from .models import movie

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']


class movieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = movie
        fields = '__all__'