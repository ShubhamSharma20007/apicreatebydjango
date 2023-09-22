from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer

# Create your views here.

class Companyviewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer