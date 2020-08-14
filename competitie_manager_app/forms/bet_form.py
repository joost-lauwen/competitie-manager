from django import forms
from competitie_manager_app.models import Bet


class BetCreateForm(forms.ModelForm):

    class Meta:
        model = Bet
        # exclude = ('match',)
        fields = ('gamble', 'stake')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gamble'].label = 'Vul je gok in'
        self.fields['stake'].label = 'Inzet'
