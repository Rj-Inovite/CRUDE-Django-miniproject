from crud import models
from django.shortcuts import render
from rest_framework import viewsets
from crud import serializers
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.customer.objects.all()
    serializer_class =serializers.CustomerSerializer

