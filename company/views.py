from django.shortcuts import render

# Create your views here.
from django.views import View


class InfoView(View):
    def get(self, request):
        return render(request, 'company/info.html')


class NewView(View):
    def get(self, request):
        return render(request, 'company/new.html')

    def post(self, request):
        type = request.POST.get('type')
        name = request.POST.get('name')
        city = request.POST.get('city')
        address = request.POST.get('address')
        wage_type = request.POST.get('wage-type')
        min_wage = request.POST.get('min-wage')
        max_wage = request.POST.get('max-wage')
        exp_time = request.POST.get('exp-time')
        edu = request.POST.get('study')
        school = request.POST.get('educ')
        key_word = request.POST.get('key-words')
        description = request.POST.get('description')
        requirement = request.POST.get('requirement')


class PositionView(View):
    def get(self, request):
        return render(request, 'company/position.html')


class ApplicantView(View):
    def get(self, request):
        return render(request, 'company/applicant.html')