from django.shortcuts import render
from django.views import generic
from django.contrib.auth import views
from django.urls import reverse_lazy
from petstagram.accounts.forms import PetstagramUserCreateForm, PetstagramUserEditForm, LoginForm
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


class UserDetailsView(generic.DetailView):
    model = PetstagramUser
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_likes = sum(p.like_set.count() for p in self.object.photo_set.all())

        context.update({
            'total_likes': total_likes,
        })

        return context


class UserEditView(generic.UpdateView):
    model = PetstagramUser
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class UserDeleteView(generic.DeleteView):
    model = PetstagramUser
    template_name = 'accounts/profile-delete-page.html'
    next_page = reverse_lazy('show home page')

    def post(self, *args, pk):
        self.request.user.delete()
