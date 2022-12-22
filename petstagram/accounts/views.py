from django.core.paginator import Paginator
from django.views import generic
from django.contrib.auth import views, get_user_model
from django.urls import reverse_lazy
from petstagram.accounts.forms import PetstagramUserCreateForm, PetstagramUserEditForm, LoginForm

UserModel = get_user_model()


class UserRegisterView(generic.CreateView):
    model = UserModel
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
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = self.object.photo_set.prefetch_related('like_set')
        total_likes = sum(photo.like_set.count() for photo in photos)
        paginated_photos =  self.object.photo_set.all()
        paginator = Paginator(paginated_photos, 2)
        page_number = self.request.GET.get('page') or 1
        page_object = paginator.get_page(page_number)
        pets_count = self.object.pet_set.count()

        context.update({
            'total_likes': total_likes,
            'paginator': paginator,
            'page_number': page_number,
            'page_object': page_object,
            'pets_count': pets_count,
        })

        return context


class UserEditView(generic.UpdateView):
    model = UserModel
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class UserDeleteView(generic.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    next_page = reverse_lazy('show home page')

    def post(self, *args, pk):
        self.request.user.delete()
