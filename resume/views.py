from django.shortcuts import render

# Create your views here.
from django.views import View


class BasicView(View):
    def get(self, request):
        return render(request, 'resume/basic.html')

    def post(self, request):
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        country = request.POST.get('country')
        phoneNum = request.POST.get('phoneNum')
        email = request.POST.get('email')


class CareerView(View):
    def get(self, request):
        return render(request, 'resume/career.html')

    def post(self, request):
        job_tpye = request.POST.get('type')
        state = request.POST.get('state')
        entry_time = request.POST.get('entry')
        cities = request.POST.getlist('city')
        wage_y_m = request.POST.get('wage_y_m')
        wage = request.POST.get('wage')
        e_wage = request.POST.get('e_wage')
        expectation = request.POST.get('expectation')


class ExperienceView(View):
    def get(self, request):
        return render(request, 'resume/experience.html')

    def post(self, request):
        job_experiences = request.POST.get('job-experiences')
        edu_experiences = request.POST.get('edu-experiences')


class SelfIntroView(View):
    def get(self, request):
        return render(request, 'resume/self_intro.html')

    def post(self, request):
        self_intro = request.POST.get('self-info')



class SkillView(View):
    def get(self, request):
        return render(request, 'resume/skill.html')

    def post(self, request):
        path = request.POST.get('path')
        exp = request.POST.get('exp')
        skill_types = request.POST.getlist('skill-type')
        skill = request.POST.get('skill')


class SocialMediaView(View):
    def get(self, request):
        return render(request, 'resume/social_media.html')

    def post(self, request):
        github = request.POST.get('github')
        blog = request.POST.get('blog')
        personal_page = request.POST.get('personal-page')
        zhihu = request.POST.get('zhihu')