from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from competitie_manager_app.models import Team


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('naam', 'sport_soort', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['naam'].label = 'Naam'
        self.fields['sport_soort'].label = 'Soort sport'
        self.fields['image'].label = 'Logo'
