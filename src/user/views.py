from django.shortcuts import render, redirect

# Create your views here.
from .forms import  SignupForm



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = SignupForm()
    return render(request, 'registration/signin.html',{'form':form})



def profile(request):
    return render(request, 'registration/profile.html')