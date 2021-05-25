from django.contrib import admin
from my_api.models import Uuid

# Register your models here.
@admin.register(Uuid)
class UuidAdmin(admin.ModelAdmin):
    list_display = ('uuid','time_created')