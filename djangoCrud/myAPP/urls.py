from django.urls import path
from .views import user_list, create_user, update_user, delete_user

urlpatterns = [
    path('users/', user_list, name='user-list'),
    path('users/create/', create_user, name='create-user'),
    path('users/<int:pk>/update/', update_user, name='update-user'),
    path('users/<int:pk>/delete/', delete_user, name='delete-user'),
]
