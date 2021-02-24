from django.core.exceptions import RequestDataTooBig
from django.forms.widgets import SplitDateTimeWidget
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import UserCreationForm, LoginForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'  لقد تمت عملية التسجيل بنجاح {username}تهانينا ')
            return redirect('home')
            
    else:
        form = UserCreationForm()

    context = {
        'title':'التسجيل',
        'form': form}
    return render (request, 'user/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm() 
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate(request, password=password, username=username)
        if user is not None:
                login(request, user) 
                return redirect('home')
        else:
            messages.warning(
                request, 'هناك خطأ في اسم المستخدم أو كلمة المرور.')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html')
    