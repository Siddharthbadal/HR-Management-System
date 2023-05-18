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
EXPERIENCE_LEVEL=(
    ('Fresher', 'Fresher'),
    ('0-2 years', '0-2 years'),
    ('2-5 years', '2-5 years'),
    ('5+ years', '5+ years'),
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




    
class Candidate(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    job = models.CharField(max_length=5)
    email = models.EmailField(max_length=30)
    age = models.CharField(max_length=3)
    mobile = models.CharField(max_length=10)

    education = models.CharField(max_length=20, choices=EDUCATION, null=True)
    city=models.CharField(max_length=30)
    salary = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=6)
    cloud = models.BooleanField(null=True, default=True)
    position= models.CharField(max_length=20, choices=POSITIONS, null=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL, null=True)

    message = models.TextField()
    file = models.FileField(upload_to="files")


    created_at=models.DateTimeField(auto_now_add=True)
    app_status= models.CharField(max_length=50, null=True, choices=STATUS, default='Pending')

    # multiselectfields
    languages = MultiSelectField(choices=LANGUAGES, default='', max_length=100)
    frameworks = MultiSelectField(choices=FRAMEWORKS, default='', max_length=100)
    databases = MultiSelectField(choices=DATABASES, default='', max_length=100)
    other_skills = MultiSelectField(choices=OTHER, default='', max_length=100)
    

    def clean(self):
        self.firstname= self.firstname.capitalize()
        self.firstname= self.firstname.strip()
        self.lastname = self.lastname.capitalize()
        self.lastname = self.lastname.strip()
        self.city = self.city.capitalize()
        self.city = self.city.strip()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


    
