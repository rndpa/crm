from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView
from .models import Report


# class IndexView(LoginRequiredMixin, CreateView):
#     model = Report
#     template_name = 'users/profile.html'
#     fields = [
#         'fio',
#         'address',
#         'revenue'
#     ]
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
