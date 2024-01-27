from rest_framework import serializers


from api.models import Telefon


class TelefonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefon
        fields = "__all__"



