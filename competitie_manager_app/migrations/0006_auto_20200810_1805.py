# Generated by Django 3.0.3 on 2020-08-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitie_manager_app', '0005_auto_20200810_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='logos/%Y/%m/%d'),
        ),
    ]
