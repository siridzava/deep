from django.urls import path
from dive_in import views


app_name = 'dive_in'
urlpatterns = [
    path('', views.index, name='index')
]