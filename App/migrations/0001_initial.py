# Generated by Django 4.2.1 on 2023-05-28 08:27

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('job', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=100)),
                ('birthdate', models.DateField(verbose_name='Date Of Birth')),
                ('mobile', models.CharField(max_length=10)),
                ('education', models.CharField(choices=[('Master', 'Master'), ('Graduate', 'Graduate'), ('Under Grad', 'Under Grad')], max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=6)),
                ('cloud', models.BooleanField(default=True, null=True)),
                ('position', models.CharField(choices=[('', 'Current Position'), ('Full Stack', 'Full Stack'), ('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Other', 'Other')], max_length=200, null=True)),
                ('experience', models.CharField(choices=[('Fresher', 'Fresher'), ('Experience', 'Experience')], max_length=200, null=True)),
                ('profile_image', models.ImageField(blank=True, default='ProfileImages/profile.png', upload_to='ProfileImages', verbose_name='ProfileImages')),
                ('message', models.TextField()),
                ('file', models.FileField(max_length=20000, upload_to='Resumes', verbose_name='Resume')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('app_status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Hold', 'Hold'), ('Rejected', 'Rejected')], default='Pending', max_length=200, null=True)),
                ('company_note', models.TextField(blank=True)),
                ('languages', multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('JavaScript', 'JavaScript'), ('Golang', 'Golang'), ('Java', 'Java'), ('C++', 'C++')], default='', max_length=100)),
                ('frameworks', multiselectfield.db.fields.MultiSelectField(choices=[('Django', 'Django'), ('React', 'React'), ('Vue', 'Vue'), ('Angular', 'Angular'), ('FastAPI', 'FastAPI')], default='', max_length=100)),
                ('databases', multiselectfield.db.fields.MultiSelectField(choices=[('MongoDB', 'MongoDB'), ('MySQL', 'MySQL'), ('PostgreSQL', 'PostgreSQL'), ('MariaDB', 'MariaDB')], default='', max_length=100)),
                ('other_skills', multiselectfield.db.fields.MultiSelectField(choices=[('Docker', 'Docker'), ('GraphQL', 'GraphQL'), ('GIT-GITHUB', 'GIT-GITHUB'), ('Jenkins', 'Jenkins'), ('Linux', 'Linux')], default='', max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('course_started', models.DateField(verbose_name='Start Date')),
                ('course_finished', models.DateField(verbose_name='End date')),
                ('course_details', models.TextField()),
                ('course_mode', models.CharField(choices=[('Regular', 'Regular'), ('correspondence', 'correspondence'), ('Distance Learning', 'Distance Learning'), ('Online', 'Online')], max_length=50)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('started_at', models.DateField(blank=True, null=True)),
                ('ended_at', models.DateField(blank=True, null=True)),
                ('notice_period', models.CharField(blank=True, max_length=2, null=True)),
                ('about_role', models.TextField(blank=True, null=True)),
                ('hybrid_office', models.BooleanField(blank=True, null=True, verbose_name='Work From Office')),
                ('still_working', models.BooleanField(blank=True, null=True, verbose_name='Currently Working')),
                ('project', models.URLField(blank=True, max_length=250, null=True)),
                ('github', models.URLField(max_length=250)),
                ('linkedin', models.URLField(max_length=250)),
                ('portfolio', models.URLField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
