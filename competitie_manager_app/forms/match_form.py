from django import forms
from competitie_manager_app.models import Match

# Form used to update a match.
class MatchUpdateForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ('h_goals', 'a_goals')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['h_goals'].label = 'Doelpunten thuis-team'
        self.fields['a_goals'].label = 'Doelpunten uit-team'
