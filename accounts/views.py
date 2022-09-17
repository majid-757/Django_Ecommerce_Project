from django.shortcuts import render, redirect
from django.views import View
import random
from django.contrib import messages



from .models import OtpCode
from .forms import UserRegistrationForm
from utils import send_top_code


class UserRegisterView(View):
    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_top_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)

            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you a code', 'success')
            return redirect('accounts:verify_code')


        return redirect('home:home')




class UserRegisterVerifyCodeView(View):
    def get(self, request):
        user_session = request.session['user_registration_info']
        print(user_session)



    def post(self, request):
        pass











