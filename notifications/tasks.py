from celery import shared_task
from django.utils import timezone
from .models import Notification
from projects.models import Project
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

@shared_task
def create_notification(actor_username,recipient_name,verb,content_type_id,object_id):
    try:
        actor = User.objects.get(username = actor_username)
        recipient = User.objects.get(username = recipient_name)
        content_type = ContentType.objects.get(id=content_type_id)
        content_object = Project.objects.get(id=object_id)

        notification = Notification.objects.create(
            receipient = recipient,
            actor = actor,
            verb = verb,
            content_type = content_type,
            content_object = content_object,
            read = False,
        )

        return notification.verb
    
    except User.DoesNotExist:
        return None
    
    except ContentType.DoesNotExist:
        return None
    
    
