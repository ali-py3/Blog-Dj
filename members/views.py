from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordsChangingform
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangingform
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/password_success.html',{})

class Register(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditeView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user