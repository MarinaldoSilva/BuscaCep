from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .Views.views_old import consultar_cep
from .Views.views import EnderecoViewSet

router = DefaultRouter()

router.register(r'consultar_cep', EnderecoViewSet)

urlpatterns = [
    path("cep/<str:cep>", consultar_cep, name="consultar-cep"),

    path('', include(router.urls))
]