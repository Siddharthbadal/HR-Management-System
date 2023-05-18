from django.contrib import admin
from .models import Candidate
from .forms import CandidateForm
from django.utils.html import format_html

# Register your models here.

class candidateAdmin(admin.ModelAdmin):
    radio_fields = {'education': admin.HORIZONTAL}
    form = CandidateForm
    # admin read only fields 
    readonly_fields = ['experience','job','firstname', 'lastname', 'email', 'gender', 'age', 'mobile', 'city', 'education','position','salary','cloud', 'languages', 'frameworks','databases','other_skills','message', 'file', 'created_at']
    # status is not the filed name but function
    exclude = ['status']
    

    list_filter=['app_status']
    list_display =['firstname', 'lastname', 'email','job', 'experience','status', '_' ]
    search_fields = ['firstname', 'lastname', 'email', 'job', 'app_status']
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