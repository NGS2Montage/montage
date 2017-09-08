from rest_framework import serializers
from jwt.exceptions import InvalidTokenError
from montage_jwt.util import decode

class JWTSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, data):
        token = data['token']
        try:
            self.claims = decode(token)
        except InvalidTokenError as err:
            raise serializers.ValidationError(str(err))

        return {
            'token': token,
        }
