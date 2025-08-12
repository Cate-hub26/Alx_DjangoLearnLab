from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserForm, ProfileForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'
    
class LoginView(AuthLoginView):
    template_name = 'login.html'

class LogoutView(AuthLogoutView):
    template_name = 'logout.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = 'login'
    
@login_required
def profile_view(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

    
