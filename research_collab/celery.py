# research_collab/celery.py

import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "research_collab.settings")

# Initialize Celery app with Redis as the broker
app = Celery("research_collab", broker="redis://localhost:6379/0")

# Load task modules from all registered Django app configs
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
