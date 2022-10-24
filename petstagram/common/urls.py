from django.urls import path
from petstagram.common.views import show_home_page, like_func, share_func, add_comment

urlpatterns = [
    path('', show_home_page, name='show home page'),
    path('like/<int:photo_id>/', like_func, name='like'),
    path('share/<int:photo_id>/', share_func, name='share'),
    path('comment/<int:photo_id>/', add_comment, name='add comment'),
]
