from rest_framework import serializers
from .models import UserNet


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """ Вывод публичной информации о пользвателе """

    class Meta:
        model = UserNet
        exclude = (
            "user_permissions",
            "groups",
            "phone",
            "email",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser"
        )


class GetUserNetSerializer(serializers.ModelSerializer):
    """ Вывод информации о пользвателе """

    class Meta:
        model = UserNet
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "user_permissions",
            "groups"
        )
