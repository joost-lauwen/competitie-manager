# Generated by Django 3.0.3 on 2020-08-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitie_manager_app', '0008_auto_20200811_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='competitie',
        ),
        migrations.AddField(
            model_name='team',
            name='competitie',
            field=models.ManyToManyField(blank=True, null=True, related_name='team_owner', to='competitie_manager_app.Competition'),
        ),
    ]
