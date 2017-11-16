from django.conf.urls import url
from django.views.generic import TemplateView

from .views import BoardApi, CardApi

urlpatterns = [
    url(r'^boards$', BoardApi.as_view()),
    url(r'^cards$', CardApi.as_view()),
    url(r'^home$', TemplateView.as_view(template_name="scrumboard/home.html")),
]