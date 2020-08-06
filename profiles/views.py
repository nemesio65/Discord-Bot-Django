from django.shortcuts import render
from .models import Profile

def profile(request):
    users = Profile.objects.all()
    return render(request, 'profiles/user_profile.html', {'users':users})
