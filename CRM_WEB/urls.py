from django.urls import path
from CRM_WEB.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]
