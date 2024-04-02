from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Message', 'Date')

    def Name(self, obj):
        return obj.first_name + " " + obj.last_name
    
    def Email(self, obj):
        return obj.email

    def Message(self, obj):
        return obj.message

    def Date(self, obj):
        return obj.created_at
    
admin.site.register(Contact, ContactAdmin)