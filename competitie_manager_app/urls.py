from django.urls import path
from django.contrib.auth import views as auth_views
from competitie_manager_app import views

app_name = 'competitie_manager_app'

urlpatterns = [
    path('',
        views.index_view.HomePage.as_view(),
        name='index'),
]
