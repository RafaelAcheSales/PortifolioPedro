from django.shortcuts import render
from django.views.generic import FormView
from .forms import SignupForm, PasswordResetCustomForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import LoginView


class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = '/accounts/signup/success/'  # Replace with your desired success URL

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

class ResetPasswordView(FormView):
    template_name = 'registration/password_reset_form.html'
    success_url = '/accounts/password_reset/done/'  # Replace with your desired success URL
    form_class = PasswordResetCustomForm
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})
    



@login_required
def profile(request):
    return render(request, 'registration/profile.html')


def home(request):
    return render(request, 'home.html')