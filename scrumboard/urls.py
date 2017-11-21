from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, CardViewSet
#
# urlpatterns = [
#     url(r'^boards$', BoardViewSet.as_view()),
#     url(r'^cards$', CardViewSet.as_view()),
# ]

router = DefaultRouter()
router.register(r'boards', BoardViewSet, base_name='boards')
router.register(r'cards', CardViewSet, base_name='cards')

urlpatterns = router.urls