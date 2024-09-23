from django.contrib import admin
from .models import SchoolData, MoreInformation, SchoolContact, Contact, FAQ

admin.site.register(SchoolData)
admin.site.register(MoreInformation)
admin.site.register(SchoolContact)

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['fio', 'tel_number', 'created']
    search_fields = ['fio', 'body', 'tel_number']

admin.site.register(FAQ)