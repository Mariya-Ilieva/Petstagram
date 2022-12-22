from django.urls import path, include
from petstagram.pets.views import AddPetView, DetailPetView, edit_pet, delete_pet

urlpatterns = [
    path('add/', AddPetView.as_view(), name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', DetailPetView.as_view(), name='details pet'),
        path('edit/', edit_pet, name='edit pet'),
        path('delete/', delete_pet, name='delete pet'),
    ])),
]
