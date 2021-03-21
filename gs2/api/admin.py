from django.contrib import admin
from .models import stduent
# Register your models here.
@admin.register(stduent)
class studenAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']