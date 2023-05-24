# Generated by Django 4.2.1 on 2023-05-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_alter_candidate_course_finished_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='still_working',
            field=models.BooleanField(blank=True, null=True, verbose_name='Currently Working'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='about_role',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hybrid_office',
            field=models.BooleanField(blank=True, null=True, verbose_name='Work From Office'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='started_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]