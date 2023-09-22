from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=  serializers.ReadOnlyField() # using this method you can read  id and show on table
    class Meta:
        model = Company
        fields= "__all__"  # it menas we are getting all varriable  name 
