from django import forms
from  django.contrib.auth.models import User



class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم ', max_length=50, help_text='لاسمح بأستخدام الرموز الخاصة ')
    email = forms.EmailField(label='الأيميل')
    last_name = forms.CharField(label='الاسم الاول ')
    first_name = forms.CharField(label='اسم العائلة')
    password1 = forms.CharField(label='كلمة المرور ', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    class Meta():
        model = User
        fields = ('username', 'email','last_name', 'first_name', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    username =  forms.CharField(max_length=100, label= 'اسم المستخدم'  )
    password =  forms.CharField( label= 'الرقم السري' , widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = (
            'username', 'password',
        )

        