from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import index

app_name = MailingConfig.name

urlpatterns = [
    path('', index)
]