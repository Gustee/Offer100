from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class CandidateRegisterForm(forms.Form):
    email = forms.EmailField(label='邮箱',
                             required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'string email optional',
                                 'id': 'talent_email',
                                 'type': 'email',
                                 'placeholder': '请输入您的邮箱地址'
                             }))
    password = forms.CharField(label='密码',
                               required=True,
                               min_length=5,
                               widget=forms.TextInput(attrs={
                                   'class': 'password optional',
                                   'id': 'talent_password',
                                   'type': 'password',
                                   'placeholder': '请输入您的密码'
                               }))
    re_password = forms.CharField(label='重复密码',
                                  required=True,
                                  min_length=5,
                                  widget=forms.TextInput(attrs={
                                        'class': 'password optional',
                                        'id': 'talent_password',
                                        'type': 'password',
                                        'placeholder': '请再次输入您的密码'
                                  }))


class HrRegisterForm(forms.Form):
    company_name = forms.CharField(label='公司名称',
                                   required=True, widget=forms.TextInput(attrs={
                                   'class': 'string optional',
                                   'id': 'recruiter_com_name',
                                   'type': 'text',
                                   'placeholder': '请输入公司名称'
                               }))
    username = forms.CharField(label='姓名',
                               required=True, widget=forms.TextInput(attrs={
                                   'class': 'string optional',
                                   'id': 'recruiter_name',
                                   'type': 'text',
                                   'placeholder': '请输入您的姓名'
                               }))
    email = forms.EmailField(label='邮箱',
                             required=True, widget=forms.TextInput(attrs={
                                 'class': 'string email optional',
                                 'id': 'talent_email',
                                 'type': 'email',
                                 'placeholder': '请输入您的邮箱地址'
                             }))
    phone = forms.IntegerField(label='电话',widget=forms.TextInput(attrs={
                                 'class': 'string tel optional phone',
                                 'id': 'recruiter_phone',
                                 'type': 'tel',
                                 'placeholder': '请输入您的手机号'
                             }))
    password = forms.CharField(label='密码',required=True,
                               min_length=5,
                               widget=forms.TextInput(attrs={
                                   'class': 'password optional',
                                   'id': 'talent_password',
                                   'type': 'password',
                                   'placeholder': '请输入您的密码'
                               }))
    re_password = forms.CharField(label='确认密码',required=True,
                                  min_length=5,
                                  widget=forms.TextInput(attrs={
                                   'class': 'password optional',
                                   'id': 'talent_password',
                                   'type': 'password',
                                   'placeholder': '请再次输入您的密码'
                                  }))


class PersionalInfoForm(forms.Form):
    name = forms.CharField()
