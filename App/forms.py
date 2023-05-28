from django import forms  
from .models import Candidate, Email
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date 
import datetime 

# convert letters to lower case
class LowerCase(forms.CharField):
    def to_python(self, value):
        return value.lower()
    
# convert letter to uppercase
class UpperCase(forms.CharField):
    def to_python(self, value):
        return value.upper()
    


class CandidateForm(forms.ModelForm):

    # validations with inside widget
    # style will apply the style-class on frontend input
    firstname = forms.CharField(
        label="First Name", 
        min_length=4, max_length=50, 
        error_messages={'required': 'First name field can not be empty.'},
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only Letters are alowed!")], 
        # required=False
        widget=forms.TextInput(attrs={'placeholder':'first name', 'style':'font-size:14px; text-transform:capitalize',  })
        )
   
    lastname = forms.CharField(
        label="Last Name", 
        min_length=4, max_length=50, 
        error_messages={'required': 'Last name field can not be empty.'},
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only Letters are alowed!")], 
        widget=forms.TextInput(attrs={'placeholder':'last name','style':'font-size:14px; text-transform:capitalize', 'autocomplete':"off"})
        )

    # using above uppercase class
    
    job = UpperCase(
        label="Job Code",
        min_length=6,
        max_length=6,
        error_messages={'required': 'Job field can not be empty.'},
        widget=forms.TextInput(attrs={'placeholder':'Job Code : SDE-01 | BAC-01','style':'font-size:14px; text-transform:uppercase', 
        'autocomplete':'off',
        'data-mask': 'AAA-00'
        })
    )
    # using lowercase class
    email = LowerCase(
        label="email ", 
        max_length=40, 
        error_messages={'required': 'Email field can not be empty.'},
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message="enter a valid email.")], 
        widget=forms.TextInput(attrs={'placeholder':'Email', 'style':'font-size:14px; text-transform:lowercase', 'autocomplete':'off'})
    )
    
    # age = forms.CharField(
    #     label="Age ", 
    #     min_length=2, max_length=2, 
    #     validators=[RegexValidator(r'^[0-9]*$', message="Only numbers are alowed!")], 
    #     widget=forms.TextInput(attrs={'placeholder':'Age'})
    # )

           

    

    mobile = forms.CharField(
        label="Contact ", 
        max_length=10, 
        error_messages={'required': 'Contact field is required.'},
        validators=[RegexValidator(r'^[0-9]*$', message="Only numbers are alowed!")], 
        widget=forms.TextInput(attrs={'placeholder':'Mobile', 'autocomplete':"off"})
    )

    message = forms.CharField(
        label="About ", 
        required=False,
        min_length=4, max_length=500, 
        widget=forms.Textarea(attrs={'placeholder':'Cover letter (optional)', 'rows':4})
    )

    city = forms.CharField(
        label="City", 
        min_length=4, max_length=50, 
        error_messages={'required': 'You must enter your current location.'},
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only Letters are alowed!")], 
        widget=forms.TextInput(attrs={'placeholder':'current city', 'style':'font-size:14px; text-transform:capitalize', 'autocomplete':"off"})
        )

    GENDER = [('M', 'Male'), ('F','Female')]
    gender= forms.CharField(label='Gender',  widget=forms.RadioSelect(choices=GENDER))
    
    cloud = forms.BooleanField(label="AWS/Azure/GCP Experience", required=False )

    file = forms.FileField(
        label='Upload CV',
        # when profile is deleted, cv images will be deleted too (by using settings.py django clearinput)
        widget=forms.ClearableFileInput(
        attrs={
            'style': 'font-size: 14px;',
            'accept': 'application/pdf, application/msword'
        })
        
    )

    profile_image = forms.FileField(
        label='Upload Image',
        widget=forms.ClearableFileInput(
            attrs={
           'style': 'font-size: 14px;',
           'accept': 'image/png, image/jpeg'
        }
        )
        
    )

    institution =forms.CharField(
        label='Institution',
        min_length=4,
        max_length=50,
        widget=forms.TextInput(

        )
    )

    course =forms.CharField(
        label='Course',
        min_length=3,
        max_length=30,        
    )

    course_details = forms.CharField(
        label="Course Details ", 
        required=False,
        min_length=4, max_length=500, 
        widget=forms.Textarea(attrs={'placeholder':'Course  structure (optional)', 'rows':4})
    )

    about_role = forms.CharField(
        label="Description", 
        required=False,
        min_length=4, max_length=500, 
        widget=forms.Textarea(attrs={'placeholder':' Roles & Responsibilities', 'rows':4})
    )


    hybrid_office = forms.BooleanField(label='Work From Office', required=False)
    still_working = forms.BooleanField(label='Currently Working', required=False)


    linkedin = LowerCase(
        label="Linkedin ", 
        max_length=100, 
        error_messages={'required': 'We need your linkedin account url.'},
        validators=[RegexValidator(r'^https://[a-z]{2,3}[.]linkedin[.]com/.*$', message="enter a valid linkedIn url.")], 
        widget=forms.TextInput(attrs={'placeholder':'linkedIn', 'style':'font-size:14px;', 'autocomplete':'off'})
    )

    github = LowerCase(
        label="Github ", 
        max_length=100, 
        error_messages={'required': 'Please enter your active github account url.'},
        validators=[RegexValidator(r'^https://[a-z]{2,3}[.]github[.]com/.*$', message="enter a valid github url.")], 
        widget=forms.TextInput(attrs={'placeholder':'github', 'style':'font-size:14px;', 'autocomplete':'off'})
    )

    project = LowerCase(
        label="Project ", 
        max_length=100,
        required=False,     
        widget=forms.TextInput(attrs={'placeholder':'recent project (optional)', 'style':'font-size:14px;' ,'autocomplete':'off'})
    )

    portfolio = LowerCase(
        label="Website ", 
        max_length=100,   
        required=False,      
        widget=forms.TextInput(attrs={'placeholder':'optional', 'style':'font-size:14px;' , 'autocomplete':'off'})
    )










    class Meta:
        model = Candidate
        fields = "__all__"
        exclude = ['created_at', 'app_status']
        labels = {
            'education':'Education',                       
        }

        SALARY =(
            
            ('', 'Current Salary'),
            ('>6 LPA', '> 6LPA'),
            ('6-12 LPA', '6-12 LPA'),
            ('12+ LPA', '12+ LPA'),
            ('Can not disclose', 'Can not disclose')
        )

        # outside widget
        widgets={
            'salary': forms.Select(
            choices=SALARY,
            attrs={
               'class': 'form-control' #bootstrap class
                
                }),
                
            'birthdate': forms.DateInput(
                attrs={
                    'style':'font-size: 14px; cursor:pointer;',
                    'type':'date',
                    'min':'1960-01-01',
                    'max':'2023-01-01'
                    
                }),

                'course_started': forms.DateInput(
                attrs={
                    'style':'font-size: 14px; cursor:pointer;',
                    'type':'date',
                    'onkeydown': 'return false',  # block text input 
                }),

                'course_finished': forms.DateInput(
                attrs={
                    'style':'font-size: 14px; cursor:pointer;',
                    'type':'date',
                    'onkeydown': 'return false',  # block text input
                }),
                'started_at': forms.DateInput(
                attrs={
                    'style':'font-size: 14px; cursor:pointer;',
                    'type':'date',
                    'onkeydown': 'return false',  # block text input
                }),
                'ended_at': forms.DateInput(
                attrs={
                    'style':'font-size: 14px; cursor:pointer;',
                    'type':'date',
                    'onkeydown': 'return false',  # block text input
                }),

        }
        














        # fields = ['firstname', 'lastname','email','age','message']

        # outside widget
        # widgets={
        #     'mobile': forms.TextInput(attrs={
        #         'style':'font-size:14px', 
        #         'placeholder':'Mobile',
        #         'data-mask': '000 000 0000'
        #         })
        # }





    # super function - over write all other function on fields
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        #1. control panel (optional method to control input and fields)
        # self.fields['message'].required=True


        #2. disable input individual fileld [ field freeze | data not sent to backend ]
        # self.fields['experience'].disabled=True

        #3. input read-only [ can send data to backend but can't change]
        # self.fields['email'].widget.attrs.update({'readonly':'readonly'})


        #4. select option placeholder in drop down
        # wont work with admin readonly_fields
        # self.fields["experience"].choices = [("", "Select your experience"),]+ list(self.fields["experience"].choices)[1:]

        # self.fields["position"].choices = [("", "Current Role"),]+ list(self.fields["position"].choices)[1:]

        

    
        #5. widget control [over write the values]
        # self.fields['mobile'].widget.attrs.update({'style':'font-size:24px;', 'placeholder':'Phone'})

        #6. freeze/disable multiple input fields 

        # readonly = ['firstname', 'lastname', 'job']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly']=True




        # disable all inpute. make candidate details read only for backend.html on frontend 
        # instance = getattr(self, 'instance', None)
        # readonly_fields = ['experience','job','firstname', 'lastname', 'email', 'gender', 'birthdate', 'mobile', 'city', 'education','position','salary','cloud', 'languages', 'frameworks','databases','other_skills','message','profile_image', 'file', 'course', 'institution', 'course_started', 'course_finished', 'course_details', 'course_mode',
        # 'company', 'role', 'started_at', 'ended_at', 'notice_period', 'about_role', 'hybrid_office', 'still_working','linkedin', 'github', 'project', 'portfolio']
        # for field in readonly_fields:
        #     if instance and instance.pk:
        #         self.fields[field].disabled=True
        # above function will not allow read only on admin as this is in super. so not accepted




# Function to validate unique email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Candidate.objects.filter(email = email).exists():
                raise forms.ValidationError('Email already registered!')

        return email 
    

    # job code validations
    def clean_job(self):
        job = self.cleaned_data.get('job')
        if job == 'SDE-01' or job == 'BAC-01' or job == 'FRE-01':
            return job
        else:
            raise forms.ValidationError('Please enter the correct code!')


    # def clean_age(self):
    #     age = self.cleaned_data.get('age')
    #     if age < '18' or age > '70':
    #         raise forms.ValidationError("Age must be between 18 to 70")
    #     return age
    
    def clean_birthdate(self):
        birth = self.cleaned_data.get('birthdate')
        b = birth
        now = date.today()
        age = (now.year - b.year) - ((now.month, now.day) <(b.month, b.day))
        if age < 18 or age > 65:
            raise forms.ValidationError("Min age: 18 Max age: 65")
        return birth 

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if len(mobile) != 10:
            raise ValidationError("Please eneter the complete mobile number")
        return mobile
    
    # def clean_file(self):
    #     file = self.cleaned_data.get('file', False)
    #     EXT = ['pdf', 'doc','docx']
    #     ext = str(file).split('.')[-1]
    #     type = ext.lower()
    #     if type not in EXT:
    #         raise forms.ValidationError("Only -PDF-DOC-DOCX files")
    #     if file.size > 2 * 1048476:
    #         raise forms.ValidationError("File should not be more than of 2 MB")


    def clean_course_started(self):
        started_course = self.cleaned_data['course_started']
        if started_course is None:
            raise forms.ValidationError("Please Select a valid date")
        if started_course > datetime.date.today():
            raise forms.ValidationError("Invalid date")
        return started_course
    
    def clean_course_finished(self):
        course_finished = self.cleaned_data['course_finished']
        if course_finished is None:
            return "Still Going On"
        if course_finished > datetime.date.today():
            raise forms.ValidationError("Invalid date")
        return course_finished
    
    def clean_started_at(self):
        started_at = self.cleaned_data['started_at']
        if started_at is None:
            raise forms.ValidationError("Please Select a valid date")
        if started_at > datetime.date.today():
            raise forms.ValidationError("Invalid date")
        return started_at
    
    def clean_ended_at(self):
        ended_at = self.cleaned_data['ended_at']
        if ended_at is None:
            ended_at = datetime.date.today()
            return ended_at
        if ended_at > datetime.date.today():
            raise forms.ValidationError("Invalid date")
        return ended_at
    

class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = "__all__"
            





