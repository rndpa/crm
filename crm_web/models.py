from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# from users.models import Profile


class Report(models.Model):
    fio = models.CharField('ФИО', max_length=500, blank=False, null=False)
    address = models.CharField('Адрес точки', max_length=1500, blank=False, null=False)
    revenue = models.FloatField('Выручка', null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return reverse('profile', kwargs={"pk": self.pk})
