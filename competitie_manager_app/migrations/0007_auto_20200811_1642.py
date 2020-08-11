# Generated by Django 3.0.3 on 2020-08-11 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitie_manager_app', '0006_auto_20200810_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='made_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='competition_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='competition',
            name='sport_soort',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sport_competitie', to='competitie_manager_app.Sport'),
            preserve_default=False,
        ),
    ]
