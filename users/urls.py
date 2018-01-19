from django.urls import path
from .views import *

urlpatterns = [
    path('basic/', PersonalInfoView.as_view()),
]