from django import forms
from competitie_manager_app.models import Bet
from competitie_manager_app.models import UserTotoInfo
from django.core.exceptions import ValidationError

class BetCreateForm(forms.ModelForm):

    class Meta:
        model = Bet
        fields = ('gamble', 'stake')
        widgets = {'gamble': forms.HiddenInput()}

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gamble'].label = 'Vul je gok in'
        self.fields['stake'].label = 'Inzet'
        self.user = user

    def clean_stake(self):
        user = self.user
        data = self.cleaned_data['stake']
        toto_points = UserTotoInfo.objects.get(user=user).toto_points

        if toto_points < data:
            raise ValidationError('Helaas, je hebt te weinig toto punten.')

        return data
