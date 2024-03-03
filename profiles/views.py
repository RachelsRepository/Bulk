from django.shortcuts import render, redirect
from .forms import UserProfileForm

def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_created')
    else:
        form = UserProfileForm()
    return render(request, 'profiles/create_profile.html', {'form': form})

def profile_created(request):
    return render(request, 'profiles/profile_created.html')

