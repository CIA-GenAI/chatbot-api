import time
from celery import shared_task, Celery

celery = Celery(
    __name__,
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)


@celery.task
def send_push_notification(device_token: str):
    time.sleep(10)  # simulates slow network call to firebase/sns
    with open("notification.log", mode="a") as notification_log:
        response = f"Successfully sent push notification to: {device_token}\n"
        notification_log.write(response)

""""
@app.get("/push/{device_token}")
async def notify(device_token: str):
    send_push_notification.delay(device_token)
    return {"message": "Notification sent"}
"""