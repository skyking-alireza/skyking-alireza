from django.shortcuts import render
from rest_framework.generics import  ListAPIView , RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from .models import PageModel
from .serializers import PageSerializer , PageListSerializer
from .permissions import RUDPagePermission
from rest_framework.permissions import IsAdminUser
from .Pagination import StandardResultsSetPagination
# Create your views here.

class CreatePageView(CreateAPIView):
    model = PageModel
    serializer_class = PageSerializer
    permission_classes = [IsAdminUser, ]

class RUDPageView(RetrieveUpdateDestroyAPIView):
    queryset = PageModel.objects.all()
    serializer_class = PageSerializer
    permission_classes = [RUDPagePermission,]


class PageListView(ListAPIView):
    queryset = PageModel.objects.all()
    serializer_class = PageListSerializer
    pagination_class = StandardResultsSetPagination


class AllPageListView(ListAPIView):
    queryset = PageModel.objects.all()
    serializer_class = PageListSerializer
