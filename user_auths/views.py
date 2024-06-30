from django.shortcuts import render, redirect
from user_auths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def RegisterView(request):
    if request.method == "POST": 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created successfully.")
            new_user = authenticate(username = form.cleaned_data.get('email'), 
                                    password=form.cleaned_data.get('password1'))
            login(request, new_user)
            return redirect("core:index")
    elif request.user.is_authenticated:
        messages.warning(request, f"You are already logged in.")
        return redirect("core:index")
    else:
        form = UserRegisterForm()
    context = {
        "signup_form": form
    }
    return render(request, "user_auths/sign-up.html", context)