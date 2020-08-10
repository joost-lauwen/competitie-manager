from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserCreateForm(UserCreationForm):

    def clean_email(self):
        data = self.cleaned_data['email']
        if '@novi.nl' not in data:
            raise ValidationError('Helaas, je kan alleen registreren met een Novi account!')

        return data

    class Meta():
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Gebruikersnaam'
        self.fields['email'].label = 'Email adres'
        self.fields['password1'].label = 'Wachtwoord'
        self.fields['password2'].label = 'Wachtwoord herhalen'
