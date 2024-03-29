import django.apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, TemplateView

from crm_web.models import Report

from datetime import date
from django.db.models import Sum

from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import redirect


def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name="admin").exists():
        # user is an admin
        return redirect("admin_profile-day")
    else:
        return redirect("profile")


class SuperuserRequiredMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(SuperuserRequiredMixin, self).dispatch(*args, **kwargs)


def summ_today(model):
    for itm in django.apps.apps.get_models():
        name = model
        count = model.objects.all()['revenue'].count()
        return count


class AdminProfileDayView(LoginRequiredMixin, SuperuserRequiredMixin, TemplateView):
    template_name = 'users/admin-profile-day.html'
    date = date.today()
    summ = Report.objects.aggregate(sum=Sum('revenue'))['sum']
    user_name = User.objects.all()
    report = Report.objects.all()

    def my_view(self, request):
        if not request.user.is_superuser:
            return render(request, 'users/profile.html')

    def get(self, request, *args, **kwargs):
        print(f'Текущий пользователь {request.user}')
        print(f'Выбранный пользователь - {request.GET.get("manager")}')
        target_user = request.GET.get("manager")
        current_user = request.user

        return render(request, 'users/admin-profile-day.html', context={
            'user_name': self.user_name,
            'report_users': self.report,
            'target_user': target_user,
            'current_user': current_user,
            'date_today': self.date
        })


class AdminProfileDateView(LoginRequiredMixin, SuperuserRequiredMixin, TemplateView):
    template_name = 'users/admin-profile-date.html'
    date = date.today()
    summ = Report.objects.aggregate(sum=Sum('revenue'))['sum']
    user_name = User.objects.all()
    report = Report.objects.all().order_by('-created_at')

    def get(self, request, *args, **kwargs):
        target_user = request.GET.get("manager")
        target_date = request.GET.get("date")
        target_month = str(request.GET.get("date"))
        current_user = request.user

        return render(request, 'users/admin-profile-date.html', context={
            'user_name': self.user_name,
            'report_users': self.report,
            'target_user': target_user,
            'target_date': target_date,
            'target_month': target_month[0:7],
            'current_user': current_user,
            'date_today': self.date
        })


class AdminProfileMonthView(LoginRequiredMixin, SuperuserRequiredMixin, TemplateView):
    template_name = 'users/admin-profile-month.html'
    date = date.today()
    summ = Report.objects.aggregate(sum=Sum('revenue'))['sum']
    user_name = User.objects.all()
    report = Report.objects.all().order_by('-created_at')

    def get(self, request, *args, **kwargs):
        target_user = request.GET.get("manager")
        target_date = request.GET.get("date")
        target_month = str(request.GET.get("date"))
        current_user = request.user

        return render(request, 'users/admin-profile-month.html', context={
            'user_name': self.user_name,
            'report_users': self.report,
            'target_user': target_user,
            'target_date': target_date,
            'target_month': target_month[0:7],
            'current_user': current_user,
            'date_today': self.date
        })


class ProfileView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'users/profile.html'
    context_object_name = 'report'
    date = date.today()
    summ = Report.objects.aggregate(sum=Sum('revenue'))['sum']
    user_name = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['date_today'] = self.date
        context['summ'] = round(self.summ, 2)
        context['user'] = self.user_name
        return context


class ProfileMonthView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile_month.html'
    context_object_name = 'report'
    date = date.today()
    summ = Report.objects.aggregate(sum=Sum('revenue'))['sum']

    def get(self, request, *args, **kwargs):
        target_user = request.GET.get("manager")
        report = Report.objects.all().order_by('-created_at')
        user_name = User.objects.all()
        target_date = request.GET.get("date")
        target_month = str(request.GET.get("date"))
        current_user = request.user

        return render(request, 'users/profile_month.html', context={
            'report': report,
            'user_name': user_name,
            'report_users': report,
            'target_user': target_user,
            'target_date': target_date,
            'target_month': target_month[0:7],
            'current_user': current_user,
            'date_today': self.date
        })


class ProfileAllView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile_all.html'
    date = date.today()
    summ = Report.objects.aggregate(sum=Sum('revenue'))['sum']
    report = Report.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(ProfileAllView, self).get_context_data(**kwargs)
        context['report'] = self.report
        context['date_today'] = self.date
        context['summ'] = round(self.summ, 2)
        return context


class CreatePost(LoginRequiredMixin, CreateView):
    model = Report
    template_name = 'users/createPost.html'
    context_object_name = 'report'
    fields = [
        'fio',
        'address',
        'revenue'
    ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('profile')


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Report
    template_name = 'users/updatePost.html'
    context_object_name = 'report'
    date = date.today()

    fields = [
        'fio',
        'address',
        'revenue'
    ]

    def get_context_data(self, **kwargs):
        context = super(UpdatePost, self).get_context_data(**kwargs)
        context['date_today'] = self.date
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('profile')
