from rest_framework import serializers
from authApp.models.user import User

class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
    