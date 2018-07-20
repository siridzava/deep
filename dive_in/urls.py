from django.urls import path
from dive_in import views
from django.contrib.auth import views as aviews

app_name = 'dive_in'
urlpatterns = [
    path('', views.index, name='index'),
    path('init/', views.initiative, name='initiative'),
    path('register/', views.register, name='registration'),
    path('login/', aviews.login, name='user_login'),
]
