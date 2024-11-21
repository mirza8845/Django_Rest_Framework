from rest_framework import serializers

from api.models import Company, Employee, Places, Categories


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model= Company
        fields = '__all__'

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model= Employee
        fields = '__all__'

class PlacesSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model= Places
        fields = '__all__'

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model= Categories
        fields = '__all__'