from django.contrib.auth import views as auth_views
from django.urls import path

from users.views import *

urlpatterns = [
    path(r'login_success/$', login_success, name='login_success'),
    # path('регистрация/', UserCreationForm.as_view(), name='register'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('admin-profile-day/', AdminProfileDayView.as_view(), name='admin_profile-day'),
    path('admin-profile-date/', AdminProfileDateView.as_view(), name='admin_profile-date'),
    path('admin-profile-month/', AdminProfileMonthView.as_view(), name='admin_profile-month'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_month/', ProfileMonthView.as_view(), name='profile_month'),
    path('profile_all/', ProfileAllView.as_view(), name='profile_all'),
    path('createpost/', CreatePost.as_view(), name='createPost'),
    path('updatepost/<slug:pk>/', UpdatePost.as_view(), name='updatePost'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # path('сброс-пароля/', ResetPassword.as_view(), name='reset_password'),
    # path('подтверждение-сброса-пароля/', ResetPasswordConfirm.as_view(), name='reset_password_confirm'),
    # path('сброс-пароля-успешно/', ResetPasswordDone.as_view(), name='reset_password_done'),
    # path('смена-пароля/', ChangePassword.as_view(), name='change_password'),
]
