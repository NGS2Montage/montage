from rest_framework import serializers
from rafter_user_service.models import Application
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

class ApplicationJWTSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True)
    secret = serializers.CharField(write_only=True)

    def validate(self, data):
        app = self.context['app']
        
        if not app.check_token(data['secret']):
            msg = 'Wrong application secret.'
            raise serializers.ValidationError(msg)

        return {
            'token': app.get_user_token()
        }

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('name', 'desc')