"""Offer100 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import *
from resume.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('active/<str:code>', ActiveUserView.as_view(), name='active'),
    path('home/', home_view, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='signin'),
    path('profiles/', include('users.urls')),
    path('account/', AccountView.as_view()),
    path('resume/basic/', BasicView.as_view()),
    path('resume/career/', CareerView.as_view()),
    path('resume/experience/', ExperienceView.as_view()),
    path('resume/info/', InfoView.as_view()),
    path('resume/self_intro/', SelfIntroView.as_view()),
    path('resume/showcase/', ShowCaseView.as_view()),
    path('resume/skill/', SkillView.as_view()),
    path('resume/social_media/', SocialMediaView.as_view()),
]
