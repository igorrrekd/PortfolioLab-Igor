from django.shortcuts import render
from django.views import View


class LandingPage(View):
    def get(self, request):
        return render(request, 'clothes/index.html')


class AddDonation(View):
    def get(self, request):
        return render(request, 'clothes/form.html')


class Login(View):
    def get(self, request):
        return render(request, 'clothes/login.html')


class Register(View):
    def get(self, request):
        return render(request, 'clothes/register.html')