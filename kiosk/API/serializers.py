from rest_framework import serializers
from .models import *


class BrandMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandMaster , ModelMaster
        feilds = '__all__'

# class ModelMasterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ModelMaster
#         feilds = '__all__'
