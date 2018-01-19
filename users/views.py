from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic.base import View
from django.contrib import auth
from .models import *
from .forms import *
from utils.email_send import send_register_email
# Create your views here.


def home_view(request):
    return render(request, 'home.html')


class RegisterView(View):
    def get(self, request):
        candidate_register_form = CandidateRegisterForm()
        hr_register_form = HrRegisterForm()
        return render(request, 'register.html',
                      {'candidate_register_form': candidate_register_form,
                       'hr_register_form': hr_register_form})

    def post(self, request):
        if request.POST.get('user_type') == 'candidate':
            candidate_register_form = CandidateRegisterForm(request.POST)
            hr_register_form = HrRegisterForm()
            if candidate_register_form.is_valid():
                username = request.POST.get('email', '')
                if User.objects.filter(username=username):
                    return render(request, 'register.html',
                                  {'candidate_register_form': candidate_register_form,
                                   'hr_register_form': hr_register_form,
                                   'msg': '该邮箱已注册'})
                password = request.POST.get('password', '')
                new_user = User.objects.create(username=username)
                new_user.password = make_password(password)
                new_user.is_active = True
                new_user.save()
                candidate = Candidate.objects.create(user=new_user)
                candidate.save()
                auth.login(request, new_user)
                send_register_email(username, "register")
                return render(request, 'talent_confirm_mail.html', {'email':username})


            else:
                return render(request, 'register.html',
                          {'candidate_register_form': candidate_register_form,
                           'hr_register_form': hr_register_form})
        else:
            candidate_register_form = CandidateRegisterForm()
            hr_register_form = HrRegisterForm(request.POST)
            if hr_register_form.is_valid():
                username = request.POST.get('email', '')
                com_name = request.POST.get('company_name', '')
                nick_name = request.POST.get('username', '')
                phone = request.POST.get('photo', '')
                if User.objects.filter(username=username):
                    return render(request, 'register.html',
                                  {'candidate_register_form': candidate_register_form,
                                   'hr_register_form': hr_register_form,
                                   'msg': '该邮箱已注册'})
                password = request.POST.get('password', '')
                new_user = User.objects.create(username=username)
                new_user.password = make_password(password)
                new_user.save()
                hr = HR(user=new_user, nick_name=nick_name, company_name=com_name, phone=phone)
                hr.save()
                #send_register_email(username, 'register')
                return render(request, 'talent_confirm_mail.html', context={'email': username})
            return render(request, 'register.html',
                          {'candidate_register_form': candidate_register_form,
                           'hr_register_form': hr_register_form})


class LoginView(View):
    def get(self, request):
        login_form = LoginForm(request.POST)
        if request.user.is_authenticated():
            return render(request, '')
        return render(request, 'signin.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user_type = request.POST.get('user_type', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    if user_type == 'candidate':
                        #候选人登陆成功
                        return HttpResponseRedirect("/home")
                    else:
                        #hr登陆成功
                        return HttpResponseRedirect('/home')
                else:
                    #用户没有激活提示用户去邮箱点击激活链接
                    return render(request, "login.html", {"login_form": LoginForm(),
                                                      "msg": "您的账号还没有使用邮箱激活"})
            else:
                #用户名或密码错误
                return render(request, "login.html", {"login_form": LoginForm(),
                                                  "msg": "用户名或密码不正确"})
        else:
            #输入不合法
            return render(request, 'login.html', {'login_form': login_form, 'msg': '您的输入不合法'})


class ActiveUserView(View):
    def get(self, request, code):
        all_records = EmailVerifyRecord.objects.filter(code=code)
        if all_records:
            for record in all_records:
                email = record.email
                user = User.objects.get(username=email)
                user.is_active = True
                new_user = Candidate.objects.get(user_id=user.id)
                new_user.save()
                auth.login(request, user)
                return HttpResponseRedirect('/home')
        else:
            return HttpResponseRedirect('/home')


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect('/')


class PersonalInfoView(View):
    def get(self, request):
        return render(request, 'persional_info.html')

    def post(self, request):
        name = request.POST.get('name', '')
        gender = request.POST.get('gender', 'male')
        education = request.POST.get('education', 'bachelor')
        city = request.POST.get('city', '')
        mobile = request.POST.get('mobile', '')
        image = request.FILES.get('image', 'default.png')

# class HomeView(View):
#     def get(self, request):
#         return render(request, 'home.html')

def home_view(request):
    return render(request, 'home.html')