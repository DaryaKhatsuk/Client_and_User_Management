from django import forms
from .models import Support, User, Client


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Логин',
                               widget=forms.TextInput(attrs={"class": "login-input", "autocomplete": "username"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={"class": "login-input", "autocomplete": "current-password"}))

    class Meta:
        model = User
        fields = ('username', 'password')


"""
Client
"""


class UpdateClientStatusForm(forms.Form):
    status = forms.ChoiceField(choices=[("В работе", "В работе"),
                                        ("Отказ", "Отказ"),
                                        ("Сделка закрыта", "Сделка закрыта"),
                                        ]
                               )

    class Meta:
        model = Client
        fields = ('username', 'email')


"""
Support
"""


class SupportForm(forms.ModelForm):
    email = forms.CharField(label='Email', widget=forms.EmailInput)
    user_text = forms.CharField(max_length=2000, label='Сообщение', widget=forms.Textarea)

    class Meta:
        model = Support
        fields = ('user_text', 'email')
