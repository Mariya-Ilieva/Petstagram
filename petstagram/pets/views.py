from django.shortcuts import render, redirect
from petstagram.accounts.models import PetstagramUser
from petstagram.common.forms import CommentForm
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetForm, PetDeleteForm


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        return redirect('profile details', pk=1)
    return render(request, 'pets/pet-add-page.html', {'form': form})


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    owner = PetstagramUser.objects.get(username=username)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
        'owner': owner,
    }
    return render(request, 'pets/pet-details-page.html', context)


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
