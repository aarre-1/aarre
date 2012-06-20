from crm.models import Company, Contact, ContactInformation
from django.contrib import admin

'''
Basically all bullshit.
'''

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'address')

admin.site.register(Company, CompanyAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'associated_company_names')

admin.site.register(Contact, ContactAdmin)

class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'title')
    
admin.site.register(ContactInformation, ContactInformationAdmin)