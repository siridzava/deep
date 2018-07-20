from django.shortcuts import render
from dive_in.forms import UserForm, ProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from dive_in.models import Character

# Create your views here.


def index(request):
    return render(request, 'dive_in/index.html')


def initiative(request):
    return render(request, 'dive_in/initiative.html')


def rp_assistant(request):
    if request.user.is_authenticated:
        characters = Character.objects.filter(user= request.user)
        return render(request, 'dive_in/rp_assistant.html',
                      context={'characters': characters})
    else:
        return render(request, 'dive_in/rp_assistant.html')


class CharacterUpdateView(UpdateView):
    form_class = ProfileForm
    model = Character
    template_name_suffix = '_form'


def play(request, pk):
    char = Character.objects.get(pk=pk)
    return render(request, 'dive_in/interface.html', context={'character': char})


def character(request):
    if request.method == 'POST':
        char_form = ProfileForm(data=request.POST)
        if char_form.is_valid():
            char = char_form.save(commit=False)
            char.user = request.user
            char.save()
            return HttpResponseRedirect(reverse('dive_in:rp_assistant'))

    else:
        char_form = ProfileForm

    return render(request, 'dive_in/character_form.html',
                      {'char_form': char_form})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        #        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid():
            #           and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            """profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()"""

            registered = True

        else:
            print(user_form.errors)
#           ,profile_form.errors)

    else:
        user_form = UserForm
        profile_form = ProfileForm

    return render(request, 'dive_in/register.html',
                  {'user_form': user_form,
#                  'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('/'))

            else:
                return HttpResponse("Account is not active")
        else:
            print('Failed attempt to login')
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'dive_in/../templates/registration/login.html', {})
