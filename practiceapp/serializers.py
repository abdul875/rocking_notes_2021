from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
