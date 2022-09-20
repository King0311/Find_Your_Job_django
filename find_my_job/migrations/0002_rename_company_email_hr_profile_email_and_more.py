# Generated by Django 4.0.7 on 2022-09-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_my_job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hr_profile',
            old_name='company_email',
            new_name='email',
        ),
        migrations.AddField(
            model_name='hr_profile',
            name='post',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='hr_profile',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='seeker_profile',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
