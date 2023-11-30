from django.urls import path
from .views import RegisterPage, CustomLoginView
from django.contrib.auth.views import LogoutView
from users import views as user_views

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', user_views.profile, name='profile')

]