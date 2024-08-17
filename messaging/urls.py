from django.urls import path
from . import views

urlpatterns = [
    path("", views.messages, name="messages"),
    path("<int:user_id>/", views.messages, name="message_detail"),
    # Keep your existing URL patterns
    path("get-messages/<int:user_id>/", views.get_messages, name="get_messages"),
    path("poll-messages/<int:user_id>/", views.poll_messages, name="poll_messages"),
    path("send-message/", views.send_message, name="send_message"),
]
