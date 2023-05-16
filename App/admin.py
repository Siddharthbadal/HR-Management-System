from django.contrib import admin
from .models import Candidate
from django.utils.html import format_html

# Register your models here.

class candidateAdmin(admin.ModelAdmin):
    list_filter=['app_status']
    list_display =['firstname', 'lastname', 'email','job', 'experience','status', '_' ]
    search_fields = ['firstname', 'lastname', 'email', 'job', 'app_status', 'app_status']
    list_per_page = 20

    # function to change icon for list display
    def _(self, obj):
        if obj.app_status == 'Approved':
            return True
        elif obj.app_status == 'Pending':
            return None
        else:
            return False
    _.boolean = True 

    # function to change text
    def status(self, obj):
        if obj.app_status == 'Approved':
            color = "#28a745"
        elif obj.app_status == 'Pending':
            color = "#fea95e"
        else:
            color ="red"
        return format_html("<strong><p style='color: {}'>{}</p></strong>".format(color, obj.app_status))
    status.allow_tags=True 
           

admin.site.register(Candidate, candidateAdmin)