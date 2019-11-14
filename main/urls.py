from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from main.views import CandidatesViewSet
from . import views

# Routers provide an easy way of automatically determining the URL conf.
urlpatterns = [
    url(r'^$', views.Registration.as_view(), name='home'),

    url(r'^api-auth/', include('rest_framework.urls'))
]

router = routers.DefaultRouter()
router.register(r'candidates', CandidatesViewSet)

urlpatterns += router.urls
