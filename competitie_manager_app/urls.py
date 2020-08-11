from django.urls import path
from django.contrib.auth import views as auth_views
from competitie_manager_app import views

app_name = 'competitie_manager_app'

urlpatterns = [
    path('',
        views.index_view.HomePage.as_view(),
        name='index'),
    path('inloggen/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'),
    path('uitloggen/',
        auth_views.LogoutView.as_view(),
        name='logout'),
    path('registreren/',
        views.register_view.SignUp.as_view(),
        name='signup'),
    path('teammaken/',
        views.CreateTeamView.as_view(),
        name='create_team'),
    path('team/<int:pk>/',
        views.TeamDetailView.as_view(),
        name='team_detail'),
    path('competitiemaken/',
        views.CreateCompetitionView.as_view(),
        name='create_competition'),
    path('competition/<int:pk>/',
        views.CompetitionDetailView.as_view(),
        name='competition_detail'),
]
