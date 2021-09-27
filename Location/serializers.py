from rest_framework import serializers
from Location.models import PhysicalLocation

class PhysicalLocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=PhysicalLocation
        fields='__all__'
