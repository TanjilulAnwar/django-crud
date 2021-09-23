from django.contrib import admin
from employee.models import Employee

class AuthorAdmin(admin.ModelAdmin):
    # pass
    list_display = ('eid','ename', 'eemail', 'econtact')
admin.site.register(Employee, AuthorAdmin)
