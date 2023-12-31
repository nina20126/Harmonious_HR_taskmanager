from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

class RegisterPage(FormView):
   template_name = 'users/register.html'
   form_class = UserCreationForm
   redirect_authenticated_user = True
   success_url = reverse_lazy('tasks')

   def form_valid(self, form):
      user = form.save()
      if user is not None:
         login(self.request, user)
      return super(RegisterPage, self).form_valid(form)
   
   def get(self, *args, **kwargs):
      if self.request.user.is_authenticated:
         return redirect('task')
      return super(RegisterPage, self).get(*args, **kwargs)
   

class CustomLoginView(LoginView):
   template_name = 'users/login.html'
   fields = '__all__'
   redirect_authenticated_user = True

   def get_success_url(self):
      return reverse_lazy('tasks')


@login_required
def profile(request):
   return render(request, 'users/profile.html')