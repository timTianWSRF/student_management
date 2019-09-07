from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'score', 'email', 'qq', 'phone',
                    'created_time')
    list_filter = ('sex', 'created_time')
    search_fields = ('name', 'score')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                ('sex', 'score'),
                ('email', 'qq', 'phone')
            )
        }),
    )
    list_editable = ['score']


admin.site.register(Student, StudentAdmin)
# Register your models here.
