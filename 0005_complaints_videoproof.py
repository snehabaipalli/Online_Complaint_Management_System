# Generated by Django 4.0.5 on 2022-07-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complaint_Management_System', '0004_alter_complaints_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='videoproof',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
