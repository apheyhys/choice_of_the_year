from django.urls import path
from . import views


urlpatterns = [
    path('year_create/', views.CreateYear.as_view()),
]
