from rest_framework import serializers  
from .models import Drink
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description')
        model = Drink