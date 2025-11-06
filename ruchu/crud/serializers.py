from crud import models 
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customer
        queryset = models.customer.objects.all()
        fields = '__all__'