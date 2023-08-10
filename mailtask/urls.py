from django.urls import include, path

from mailtask.views import ReviewView

urlpatterns = [
    path("", ReviewView.as_view(), name='review'),
]
