from django.urls import path
from .views import UserCreateView, UserListView, ContactCreateView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("contact/create/", ContactCreateView.as_view(), name="contact-create"),
]
