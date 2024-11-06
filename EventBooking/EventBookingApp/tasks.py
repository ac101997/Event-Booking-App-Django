from celery import shared_task

import time


@shared_task
def email_send(email):
    msg="Booking successful"
    print(f"sending email to {email}")
    time.sleep(5)
    print(f"sent email to {email}")