from django import forms  
from .models import Candidate
from django.core.validators import RegexValidator


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
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only Letters are alowed!")], 
        # required=False
        widget=forms.TextInput(attrs={'placeholder':'first name', 'style':'font-size:14px; text-transform:capitalize'})
        )
   
    lastname = forms.CharField(
        label="Last Name", 
        min_length=4, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only Letters are alowed!")], 
        widget=forms.TextInput(attrs={'placeholder':'last name','style':'font-size:14px; text-transform:capitalize'})
        )

    # using above uppercase class
    
    job = UpperCase(
        label="Job Code",
        min_length=5,
        max_length=5,
        widget=forms.TextInput(attrs={'placeholder':'Job Code','style':'font-size:14px; text-transform:uppercase'})
    )
    # using lowercase class
    email = LowerCase(
        label="email ", 
        max_length=20, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message="enter a valid email")], 
        widget=forms.TextInput(attrs={'placeholder':'Email', 'style':'font-size:14px; text-transform:lowercase'})
    )
    
    age = forms.CharField(
        label="Age ", 
        min_length=2, max_length=2, 
        validators=[RegexValidator(r'^[0-9]*$', message="Only numbers are alowed!")], 
        widget=forms.TextInput(attrs={'placeholder':'Age'})
    )
    mobile = forms.CharField(
        label="Contact ", 
        max_length=10, 
        validators=[RegexValidator(r'^[0-9]*$', message="Only numbers are alowed!")], 
        widget=forms.TextInput(attrs={'placeholder':'Mobile'})
    )

    message = forms.CharField(
        label="About ", 
        required=False,
        min_length=4, max_length=500, 
        widget=forms.Textarea(attrs={'placeholder':'Your Skills summary', 'rows':4})
    )

    city = forms.CharField(
        label="City", 
        min_length=4, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only Letters are alowed!")], 
        widget=forms.TextInput(attrs={'placeholder':'current city', 'style':'font-size:14px; text-transform:capitalize'})
        )

    GENDER = [('M', 'Male'), ('F','Female')]
    gender= forms.CharField(label='Gender',  widget=forms.RadioSelect(choices=GENDER))
    
    cloud = forms.BooleanField(label="AWS/Azure/GCP Experience", required=False )

    file = forms.FileField(
        label='Upload CV',
        widget=forms.ClearableFileInput(
        attrs={
            'style': 'font-size: 18px;'
        })
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
                
                })
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





    # super function
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










            
    # using form widget
    # job = forms.CharField(
    #     label="Job Code",
    #     min_length=5,
    #     max_length=5,
    #     widget=forms.TextInput(attrs={'placeholder':'Job Code'})
    # )
    