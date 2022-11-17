from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.creat(user=user)
            return redirect("/log-in/")
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "userprofile/signup.html", context)
