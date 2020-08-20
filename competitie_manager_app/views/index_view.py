from django.views.generic import TemplateView

# Class to render the default home page
class HomePage(TemplateView):
    template_name = 'index.html'
