from django.urls import path
from .views import UserCreateView, UserListView, ContactCreateView, BlogListView, BlogDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("contact/create/", ContactCreateView.as_view(), name="contact-create"),
    path("blogs/", BlogListView.as_view(), name='blog-list'),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name='blog-detail'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)