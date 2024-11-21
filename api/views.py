from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Company, Employee, Places, Categories
from api.serializers import CompanySerializer, EmployeeSerializer, PlacesSerializer, CategoriesSerializer


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        try:
            company=Company.objects.get(pk=pk)
            employees=Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(employees, many=True, context={'request': request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer