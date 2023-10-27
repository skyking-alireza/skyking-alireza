from django.urls import path
from .views import CreatePageView, RUDPageView, PageListView, AllPageListView
urlpatterns = [
    path('CreatePage',CreatePageView.as_view()),
    path('RUDPage/<pk>',RUDPageView.as_view()),
    path('PageList',PageListView.as_view()),
    path('AllPageList',AllPageListView.as_view()),
]