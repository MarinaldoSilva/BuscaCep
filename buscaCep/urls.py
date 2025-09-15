from django.urls import path
from .Views.views_old import consultar_cep

urlpatterns = [
    path("cep/<str:cep>", consultar_cep, name="consultar-cep")
]