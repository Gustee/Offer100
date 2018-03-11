from django.urls import path
from .views import *

urlpatterns = [
    path('personal_info/', PersonalInfoView.as_view()),
    path('account/', AccountView.as_view()),
    path('career_info/', CareerInfoView.as_view()),
    path('experience/',Experience.as_view()),
]