from django.db import models
from multiselectfield import MultiSelectField

STATUS = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Hold', 'Hold'),
    ('Rejected', 'Rejected'),
)
EDUCATION=(
    ('Master','Master'),
    ('Graduate','Graduate'),
    ('Under Grad','Under Grad'),
)
POSITIONS = (
    ('', 'Current Position'),
    ('Full Stack','Full Stack'),
    ('Frontend','Frontend'),
    ('Backend','Backend'),
    ('Other','Other'),
)
# EXPERIENCE_LEVEL=(
#     ('Fresher', 'Fresher'),
#     ('0-2 years', '0-2 years'),
#     ('2-5 years', '2-5 years'),
#     ('5+ years', '5+ years'),
# )
EXPERIENCE_LEVEL=(
    ('Fresher', 'Fresher'),
    ('Experience', 'Experience'),
    
)

FRAMEWORKS =(
    ('Django','Django'),
    ('React','React'),
    ('Vue','Vue'),
    ('Angular','Angular'),
    ('FastAPI','FastAPI'),
)
DATABASES = (
    ('MongoDB','MongoDB'),
    ('MySQL','MySQL'),
    ('PostgreSQL','PostgreSQL'),
    ('MariaDB','MariaDB'),
)
LANGUAGES=(
    ('Python','Python'),
    ('JavaScript','JavaScript'),
    ('Golang','Golang'),
    ('Java','Java'),
    ('C++', 'C++'),
)
OTHER =(    
    ('Docker','Docker'),
    ('GraphQL','GraphQL'),
    ('GIT-GITHUB','GIT-GITHUB'),
    ('Jenkins','Jenkins'),
    ('Linux', 'Linux'),
)

COURSE_MODE=(
    ('Regular','Regular'),
    ('correspondence','correspondence'),
    ('Distance Learning','Distance Learning'),
    ('Online','Online'),
)



    
class Candidate(models.Model):
    # personal details
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    job = models.CharField(max_length=6)
    email = models.EmailField(max_length=100)
    birthdate = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Date Of Birth')
    mobile = models.CharField(max_length=10)

    education = models.CharField(max_length=100, choices=EDUCATION, null=True)
    city=models.CharField(max_length=100)
    salary = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=6)
    cloud = models.BooleanField(null=True, default=True)
    position= models.CharField(max_length=200, choices=POSITIONS, null=True)
    experience = models.CharField(max_length=200, choices=EXPERIENCE_LEVEL, null=True)

    profile_image = models.ImageField(upload_to='ProfileImages', verbose_name='ProfileImages', blank=True, default='ProfileImages/profile.png')
    message = models.TextField()
    file = models.FileField(upload_to="Resumes", verbose_name="Resume", max_length=20000)

    created_at=models.DateTimeField(auto_now_add=True)
    app_status= models.CharField(max_length=200, null=True, choices=STATUS, default='Pending')
    company_note = models.TextField(blank=True)
    # admin_verifier = models.CharField(max_length=100)

    # skils - multiselectfields
    languages = MultiSelectField(choices=LANGUAGES, default='', max_length=100)
    frameworks = MultiSelectField(choices=FRAMEWORKS, default='', max_length=100)
    databases = MultiSelectField(choices=DATABASES, default='', max_length=100)
    other_skills = MultiSelectField(choices=OTHER, default='', max_length=100)

    # education
    course = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    course_started = models.DateField(auto_now=False, auto_now_add=False,verbose_name='Start Date')
    course_finished = models.DateField(auto_now=False, auto_now_add=False, verbose_name='End date')
    course_details= models.TextField()
    course_mode = models.CharField(max_length=50, null=False, choices = COURSE_MODE)



    # experience - work
    company = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    started_at =models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    ended_at = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    notice_period = models.CharField(max_length=2, null=True, blank=True)
    about_role= models.TextField(null=True, blank=True)
    hybrid_office = models.BooleanField(null=True, blank=True, verbose_name="Work From Office")
    still_working = models.BooleanField(null=True, blank=True, verbose_name="Currently Working")



    # connect
    project = models.URLField(max_length=250, null=True, blank=True)
    github= models.URLField(max_length=250)
    linkedin= models.URLField(max_length=250)
    portfolio= models.URLField(max_length=250, null=True, blank=True)




    def __str__(self):
        return self.firstname
    

    def clean(self):
        self.firstname= self.firstname.capitalize()
        self.firstname= self.firstname.strip()
        self.lastname = self.lastname.capitalize()
        self.lastname = self.lastname.strip()
        self.city = self.city.capitalize()
        self.city = self.city.strip()

    
    
    # concatnate first namd nad lastname for admin
    def name(obj):
        return "%s %s" % (obj.firstname, obj.lastname)
    
    # concate name for candidate profile in admin
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    


    
