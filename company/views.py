from django.shortcuts import render

# Create your views here.
from django.views import View


class InfoView(View):
    def get(self, request):
        return render(request, 'company/info.html')


class NewView(View):
    def get(self, request):
        return render(request, 'company/new.html')


class PositionView(View):
    def get(self, request):
        return render(request, 'company/position.html')


class ApplicantView(View):
    def get(self, request):
        return render(request, 'company/applicant.html')