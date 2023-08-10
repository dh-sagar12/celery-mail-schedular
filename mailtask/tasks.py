from celery import shared_task
from time import sleep
from celery.utils.log import get_task_logger
from .email import send_review_email

logger = get_task_logger(__name__)

@shared_task
def send_review_email_task(name, email, review):
    send_review_email(email=email, name=name, review=review)
    logger.info(f'Sending Email to {name} with email {email} with review {review}')
