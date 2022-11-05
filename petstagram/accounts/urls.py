from django.urls import path, include
from petstagram.accounts import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user login'),
    path('logout/', views.UserLogoutView.as_view(), name='user logout'),
    path('register/', views.UserRegisterView.as_view(), name='user register'),
    path('profile/<int:pk>/', include(
        [
            path('', views.UserDetailsView.as_view(), name='profile details'),
            path('edit/', views.UserEditView.as_view(), name='profile edit'),
            path('delete/', views.delete_profile, name='profile delete'),
        ])),
]
