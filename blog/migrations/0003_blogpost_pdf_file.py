# Generated by Django 3.2 on 2023-09-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
