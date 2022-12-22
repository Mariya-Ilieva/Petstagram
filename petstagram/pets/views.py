from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

from petstagram.common.forms import CommentForm
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetForm, PetDeleteForm

UserModel = get_user_model()


class AddPetView(CreateView):
    template_name = 'pets/pet-add-page.html'
    form_class = PetForm
    model = Pet

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return redirect('details user', self.request.user.pk)


class DetailPetView(DetailView):
    template_name = 'pets/pet-details-page.html'
    model = Pet

    def get_context_data(self, **kwargs):
        all_photos = self.object.photo_set.all()
        photos_count = all_photos.count()
        comment_form = CommentForm()
        owner = self.object.user

        context = {
            'photos_count': photos_count,
            'all_photos': all_photos,
            'comment_form': comment_form,
            'owner': owner,
        }

        return context


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username, pet_slug)
    return render(request, 'pets/pet-edit-page.html', {'form': form})


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    return render(request, 'pets/pet-delete-page.html', {'form': form})
