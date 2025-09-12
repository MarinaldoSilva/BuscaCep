from .models import Endereco
from rest_framework import serializers

class EnderecoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fileds = '__all__'
        