from rest_framework import serializers
from . import const_models

# class CountrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = const_models.Country
#         fields ="__all__" 

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = const_models.State
        fields ="__all__" 

class LocalAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = const_models.LocalArea
        fields ="__all__" 





