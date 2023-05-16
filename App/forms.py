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
    firstname = forms.CharField(
        label="First Name", 
        min_length=4, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only Letters are alowed!")], 
        # required=False
        widget=forms.TextInput(attrs={'placeholder':'first name'})
        )
   
    lastname = forms.CharField(
        label="Last Name", 
        min_length=4, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only Letters are alowed!")], 
        widget=forms.TextInput(attrs={'placeholder':'last name'})
        )

    # using above uppercase class
    job = UpperCase(
        label="Job Code",
        min_length=5,
        max_length=5,
        widget=forms.TextInput(attrs={'placeholder':'Job Code'})
    )
    # using lowercase class
    email = LowerCase(
        label="email ", 
        max_length=20, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message="enter a valid email")], 
        widget=forms.TextInput(attrs={'placeholder':'Email'})
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
        min_length=4, max_length=500, 
        required=False,
        widget=forms.Textarea(attrs={'placeholder':'Summary of your skills and expertise', 'rows':4})
    )

    city = forms.CharField(
        label="City", 
        min_length=4, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only Letters are alowed!")], 
        widget=forms.TextInput(attrs={'placeholder':'Your City'})
        )

    GENDER = [('M', 'Male'), ('F','Female')]
    gender= forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER))
    
    cloud = forms.BooleanField(label="AWS/Azure/GCP Experience", required=False)

    class Meta:
        model = Candidate
        fields = "__all__"
        exclude = ['created_at', 'app_status']

        SALARY =(
            ('Fresher', 'Fresher'),
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













            
    # using form widget
    # job = forms.CharField(
    #     label="Job Code",
    #     min_length=5,
    #     max_length=5,
    #     widget=forms.TextInput(attrs={'placeholder':'Job Code'})
    # )
    