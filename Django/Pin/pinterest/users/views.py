from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSignUpForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"you a created an account")
            return redirect('login')
        else:
            messages.warning(request, "Error in the inputes")

    else:
        form = UserSignUpForm()

    return render(request, 'users/signup.html', {'form': form})



# def login(request):

#     return render(request, "users/login.html")
