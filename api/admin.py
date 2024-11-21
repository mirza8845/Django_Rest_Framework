from django.contrib import admin
from api.models import Company, Employee, Places, Categories


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
    list_filter = ('company',)

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'created_at')
    search_fields = ('title',)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at')
    search_fields = ('title',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Places,PlacesAdmin)
admin.site.register(Categories,CategoriesAdmin)
