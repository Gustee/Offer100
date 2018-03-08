from django.shortcuts import render

# Create your views here.
from django.views import View


class BasicView(View):
    def get(self, request):
        return render(request, 'resume/basic.html')

    def post(self, request):
        pass


class CareerView(View):
    def get(self, request):
        return render(request, 'resume/career.html')

    def post(self, request):
        pass


class ExperienceView(View):
    def get(self, request):
        return render(request, 'resume/experience.html')

    def post(self, request):
        pass


class InfoView(View):
    def get(self, request):
        return render(request, 'resume/info.html')

    def post(self, request):
        pass


class SelfIntroView(View):
    def get(self, request):
        return render(request, 'resume/self_intro.html')

    def post(self, request):
        pass


class ShowCaseView(View):
    def get(self, request):
        return render(request, 'resume/showcase.html')

    def post(self, request):
        pass


class SkillView(View):
    def get(self, request):
        return render(request, 'resume/skill.html')

    def post(self, request):
        pass


class SocialMediaView(View):
    def get(self, request):
        return render(request, 'resume/social_media.html')

    def post(self, request):
        pass