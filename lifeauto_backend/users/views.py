from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import User, Contact,Blog
from .serializers import UserSerializer, ContactSerializer,BlogSerializer



class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.filter(active=True) 
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
class BlogDetailView(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)  
        serializer = BlogSerializer(blog)
        return Response(serializer.data)