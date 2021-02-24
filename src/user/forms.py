from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms.widgets import PasswordInput

User = get_user_model()

class  SignupForm(UserCreationForm):
    username = forms.CharField(label='اسم االمستخدم ', help_text='يجب ان  لا يحتوي على رموز خاصة او مسافات فارغة ')
    password1 = forms.CharField(min_length=8 ,widget=PasswordInput, help_text='يجب ان يحتوي على احرف كبيرة واحرف صغيرة وارقام ', label='كلمة مرور ')
    password2 = forms.CharField(min_length=8 ,widget=PasswordInput, help_text='تأكد من ان كلمة المرور متابقة  ', label='تأكيد كلمة المرور ')
    frist_name = forms.CharField(max_length=150, required=False, label='الاسم الأول' ,help_text='اختياري')
    last_name = forms.CharField(max_length=150, required=False, label='الاسم الثاني' ,help_text='اختياري')
    email = forms.EmailField(max_length=254,label='البريد الالكتروني', help_text='تأكد من صحة البريد الالكتروني')


    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2', 'frist_name', 'last_name', 'email'
        )

