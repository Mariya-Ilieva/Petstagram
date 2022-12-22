from pyperclip import copy
from django.shortcuts import render, redirect, resolve_url
from petstagram.common.models import Like
from petstagram.common.forms import CommentForm, SearchForm
from petstagram.photos.models import Photo


def show_home_page(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()
    all_liked_photos = Like.objects.all()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pet__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'all_photos': all_photos,
        'form': comment_form,
        'form2': search_form,
        'all_liked_photos': all_liked_photos,
    }
    return render(request, 'common/home-page.html', context=context)


def like_func(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()
    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def share_func(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()
        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
