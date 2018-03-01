
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import SvtUnit

from import_export import resources
from import_export.fields import Field

class SvtUnitResource(resources.ModelResource):
    bar_code= Field(column_name='bc')
    class Meta:
        model = SvtUnit
        fields = ['bc']

@admin.register(SvtUnit)
class SvtUnitAdmin(ImportExportModelAdmin):
    resource_class = SvtUnitResource

