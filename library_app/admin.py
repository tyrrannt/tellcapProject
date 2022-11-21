from django.contrib import admin

from library_app.models import UnitChildModel, UnitMainModel

# Register your models here.

admin.site.register(UnitChildModel)
admin.site.register(UnitMainModel)
