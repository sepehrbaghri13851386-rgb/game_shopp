from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('reply/<int:comment_id>/', views.reply_comment, name='reply_comment'),
]