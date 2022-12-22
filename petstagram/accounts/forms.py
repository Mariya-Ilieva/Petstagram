from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms

UserModel = get_user_model()


class PetstagramUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'email']


class PetstagramUserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender']
        exclude = ['password']
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Image',
            'gender': 'Gender',
        }


class PetstagramUserDeleteForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = []


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'placeholder': 'Username',
    }))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password',
        'placeholder': 'Password',
    }))
