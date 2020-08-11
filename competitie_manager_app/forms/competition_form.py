from django import forms
from competitie_manager_app.models import Competition


class CompetitionCreateForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ('naam', 'sport_soort')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['naam'].label = 'Naam'
        self.fields['sport_soort'].label = 'Soort sport'
