from django.contrib import admin
from .models import Homework


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('hw',)


admin.site.register(Homework, HomeworkAdmin)

# Register your models here.
