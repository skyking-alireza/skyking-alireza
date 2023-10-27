from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser
from .models import BlogModel, BlogCommentModel
from .serializers import BlogSerializers, BlogCommentSerializers, BlogListSerializers
from pages.permissions import RUDPagePermission
from pages.Pagination import StandardResultsSetPagination
# Create your views here.

class BlogCreateView(CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
    permission_classes = [IsAdminUser, ]

class RUDBlogView(RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
    permission_classes = [RUDPagePermission,]

class ListBlogsView(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogListSerializers
    pagination_class = StandardResultsSetPagination
