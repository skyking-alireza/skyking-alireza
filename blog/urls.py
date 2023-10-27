from django.urls import path
from .views import BlogCreateView, RUDBlogView
urlpatterns = [
    path('BlogCreate',BlogCreateView.as_view()),
    path('RUDBlog/<pk>',RUDBlogView.as_view()),
]