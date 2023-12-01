from rest_framework import serializers
from .models import*
from OpsUser.models import OpsUser

class SignupClient(serializers.ModelSerializer):
    class Meta:
        model = ClientSignup
        fields ="__all__"
        extra_kwargs = {'password': {'write_only': True}}

class ShowFilesSerializers(serializers.ModelSerializer):
    class Meta:
        models = OpsUser
        fields = ('id', 'uploaded_by', 'file_upload')