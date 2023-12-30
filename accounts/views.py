from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is None:
            return Http404("رمز نادرست")
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))
    else:
        if request.user.is_authenticated:
            return HttpResponse("قیلا وارد شدید")
        else:
            return render(request, 'accounts/login.html', {})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

@login_required
def profile_details(request):
    profile = request.user.profile
    context = {
        profile: 'profile'
    }
    return render(request, 'accounts/profile_details.html', context)
