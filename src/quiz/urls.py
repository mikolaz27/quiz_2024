from django.urls import include, path

from quiz.views import bitcoin, normalize_emails

urlpatterns = [
    path("bitcoin/", bitcoin, name='bitcoin'),
    path("email/", normalize_emails, name='normalize_emails'),
]
