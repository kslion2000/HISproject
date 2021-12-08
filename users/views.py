from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import New_userForm
from users.models import New_user
import os

def register(request):
    if request.method == 'POST':
        form = New_userForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = New_userForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def appointment(request):
    user_id = request.user.id
    user_info = New_user.objects.get(user_ptr_id=user_id)
    user_form = New_userForm(instance=user_info)
    return render(request, 'users/appointment.html', locals())