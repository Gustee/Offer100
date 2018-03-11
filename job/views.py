from django.shortcuts import render

# Create your views here.
from django.views import View


class JobsView(View):
    def get(self, request):
        return render(request, 'job/jobs.html')


class DetailView(View):
    def get(self, request, id):
        return render(request, 'job/details.html')