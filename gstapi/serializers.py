from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'state', 'state_code', 'cost', 'gst_amount')
        # fields = '__all__'