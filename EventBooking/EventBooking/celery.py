import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventBooking.settings')

app=Celery('EventBooking')


app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks from all installed Django apps
app.autodiscover_tasks()