from django.urls import path
from dive_in import views
from django.contrib.auth import views as aviews

app_name = 'dive_in'
urlpatterns = [
    path('', views.index, name='index'),
    path('roleplay', views.rp_assistant, name='rp_assistant'),
    path('init/', views.initiative, name='initiative'),
    path('register/', views.register, name='registration'),
    path('login/', aviews.login, name='user_login'),
    path('logout/', aviews.logout, name='logout', kwargs={'next_page': 'dive_in:rp_assistant'}),
    path('character/', views.character, name='character'),
    path('character/<int:pk>', views.CharacterUpdateView.as_view(), name='update'),
    path('play/<int:pk>', views.play, name='play')

]
