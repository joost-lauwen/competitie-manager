from django import forms
from competitie_manager_app.models import Team

# Form to create a team.
class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('naam', 'sport_soort', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['naam'].label = 'Naam'
        self.fields['sport_soort'].label = 'Soort sport'
        self.fields['image'].label = 'Logo'
