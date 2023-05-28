from django.contrib import admin
from .models import Candidate, Email
from .forms import CandidateForm, EmailForm
from django.utils.html import format_html

# Register your models here.

class candidateAdmin(admin.ModelAdmin):
    radio_fields = {'education': admin.HORIZONTAL}
    form = CandidateForm   
    

    list_filter=['app_status']
    list_display =['name', 'email','job', 'experience','status', '_' ] 
    # above name is a function comes from models
    search_fields = ['firstname', 'lastname', 'email', 'job', 'app_status']
    list_per_page = 20

    # admin read only fields 
    readonly_fields = ['experience','job','firstname', 'lastname', 'email', 'gender', 'birthdate', 'mobile', 'city', 'education','position','salary','cloud', 'languages', 'frameworks','databases','other_skills','message','profile_image', 'file', 'course', 'institution', 'course_started', 'course_finished', 'course_details', 'course_mode',
    'company', 'role', 'started_at', 'ended_at', 'notice_period', 'about_role', 'hybrid_office', 'still_working','created_at', 'linkedin', 'github', 'project', 'portfolio']
    # status is not the filed name but function
    exclude = ['status']

    # admin feilds set
    fieldsets = [
        # admin only
        ('ADMIN', {'fields': ['app_status', 'company_note']}),
        ('PERSONAL', {'fields': ['experience','job','firstname', 'lastname', 'email','birthdate', 'gender',  'mobile', 'city', 'education','position','salary', 'profile_image', 'file','message']}),
        ('SKILLS', {'fields': ['languages', 'frameworks','databases','other_skills']}),
        ('EDUCATION', {'fields': ['course', 'institution', 'course_started', 'course_finished', 'course_details', 'course_mode']}),
        ('EXPERIENCE', {'fields': ['company', 'role', 'started_at', 'ended_at', 'notice_period', 'about_role', 'hybrid_office', 'still_working']}),
        ('CONNECT', {'fields': ['linkedin', 'github', 'project', 'portfolio']})

    ]

    # function to change icon for list display
    def _(self, obj):
        if obj.app_status == 'Approved':
            return True
        elif obj.app_status == 'Pending':
            return None
        elif obj.app_status == 'Hold':
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
        elif obj.app_status == 'Hold':
            color = "#0047AB"
        elif obj.app_status == 'Disapproved':
            color = "#780000"
        else:
            color ="red"
        return format_html("<strong><p style='color: {}'>{}</p></strong>".format(color, obj.app_status))
    status.allow_tags=True 
           


class EmailAdmin(admin.ModelAdmin):
    read_only = ( 'name', 'email', 'subject', 'message')
    list_display = ['name', 'email', 'subject', 'status']
    search_fields = ['name', 'email', 'subject']
    list_filter = ['status']
    list_per_page = 10




admin.site.register(Candidate, candidateAdmin)
admin.site.register(Email, EmailAdmin)