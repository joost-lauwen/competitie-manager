# Generated by Django 3.0.3 on 2020-08-14 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitie_manager_app', '0018_match_is_finished'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stake', models.IntegerField(default=1, null=True)),
                ('gamble', models.IntegerField(default=1, null=True)),
                ('bet_result', models.BooleanField(default=False)),
                ('quotation_h_team', models.DecimalField(decimal_places=2, max_digits=9999)),
                ('quotation_a_team', models.DecimalField(decimal_places=2, max_digits=9999)),
                ('quotation_draw', models.DecimalField(decimal_places=2, max_digits=9999)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bet_match', to='competitie_manager_app.Match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gambler', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]