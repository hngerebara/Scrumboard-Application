from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, CardViewSet

# urlpatterns = [
#     url(r'^boards$', BoardApi.as_view()),
#     url(r'^cards$', CardApi.as_view()),
# ]

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = router.urls