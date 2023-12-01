from rest_framework import serializers
from OpsUser.models import*
class SignupOps(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}


class SerializersFileData(serializers.ModelSerializer):
    class Meta:
        model = OpsUser
        fields = ('id', 'uploaded_by', 'file_upload')