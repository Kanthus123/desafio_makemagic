from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^personagem$', PersonagensList.as_view()),
    url(r'^personagem/(?P<pk>[0-9]+)$', PersonagensDetalhes.as_view()),
]