from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from competitie_manager_app.forms.user_creation_form import UserCreateForm
from competitie_manager_app.models.user_toto_info import UserTotoInfo


class SignUp(FormView):
    form_class = UserCreateForm
    success_url = reverse_lazy('competitie_manager_app:index')
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        UserTotoInfo.objects.create(user=form.instance)
        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())
