from django.contrib.auth import get_user_model
from rest_framework import serializers

from account.models import CustomUser
from account.utils import send_confirmation_email

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True, required=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password_confirm')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError('Passwords do not match')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(email=email, password=password)
        code = user.activation_code
        send_confirmation_email(user.email, code)
        return user


