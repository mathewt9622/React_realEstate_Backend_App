from rest_framework import serializers
from realestate.models import RealEsModel


class RealSerializer(serializers.ModelSerializer):
    class Meta:
        model=RealEsModel
        fields=(
        'Title',
        'Description',
        'Price',
        'Property',
        'Location',
        'Bedroom',
        'Bathrooms'
        )