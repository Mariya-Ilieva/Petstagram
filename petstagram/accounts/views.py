from django.shortcuts import render
from django.views import generic
from django.contrib.auth import views
from django.urls import reverse_lazy
from petstagram.accounts.forms import PetstagramUserCreateForm, LoginForm
from petstagram.accounts.models import PetstagramUser


class UserRegisterView(generic.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('user login')


class UserLoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('show home page')


class UserLogoutView(views.LogoutView):
    next_page = reverse_lazy('show home page')


def details_profile(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
