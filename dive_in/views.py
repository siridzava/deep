from django.shortcuts import render
from dive_in.forms import UserForm, ProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    return render(request, 'dive_in/index.html')


def initiative(request):
    return render(request, 'dive_in/initiative.html')


def rp_assistant(request):
    return render(request, 'dive_in/rp_assistant.html')


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
