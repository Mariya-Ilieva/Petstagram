from django.urls import path, include
from petstagram.accounts import views

urlpatterns = [
    path('login/', views.login_user, name='user login'),
    path('register/', views.register_user, name='user register'),
    path('profile/<int:pk>/', include(
        [
            path('', views.details_profile, name='profile details'),
            path('edit/', views.edit_profile, name='profile edit'),
            path('delete/', views.delete_profile, name='profile delete'),
        ])),
]
