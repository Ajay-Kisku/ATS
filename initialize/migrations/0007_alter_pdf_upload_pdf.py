# Generated by Django 4.2.4 on 2023-08-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initialize', '0006_alter_pdf_upload_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf_upload',
            name='pdf',
            field=models.ImageField(upload_to='pdfs/'),
        ),
    ]
