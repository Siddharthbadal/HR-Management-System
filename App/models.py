from django.db import models

STATUS = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Disapproved', 'Disapproved'),
)
EDUCATION=(
    ('Master','Master'),
    ('Graduate','Graduate'),
    ('Under Grad','Under Grad'),
)
POSITIONS = (
    ('Full Stack','Full Stack'),
    ('Frontend','Frontend'),
    ('Backend','Backend'),
    ('Testing','Testing'),
    ('Other','Other'),
)
EXPERIENCE_LEVEL=(
    ('Fresher', 'Fresher'),
    ('0-2 years', '0-2 years'),
    ('2-5 years', '2-5 years'),
    ('5+ years', '5+ years')
)
    
class Candidate(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    job = models.CharField(max_length=5)
    email = models.EmailField(max_length=30)
    age = models.CharField(max_length=3)
    mobile = models.CharField(max_length=10)

    education = models.CharField(max_length=20, choices=EDUCATION, default='Graduate', null=True)
    city=models.CharField(max_length=30)
    salary = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=6)
    cloud = models.BooleanField(null=True, default=True)
    position= models.CharField(max_length=20, choices=POSITIONS, default='Frontend', null=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL, default='0-2 years', null=True)

    message = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    app_status= models.CharField(max_length=50, null=True, choices=STATUS, default='Pending')

    def clean(self):
        self.firstname= self.firstname.capitalize()
        self.firstname= self.firstname.strip()
        self.lastname = self.lastname.capitalize()
        self.lastname = self.lastname.strip()
        self.city = self.city.capitalize()
        self.city = self.city.strip()

    def __str__(self):
        return self.firstname


    
