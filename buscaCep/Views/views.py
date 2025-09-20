from rest_framework import viewsets, status
from rest_framework.response import Response

from ..serializers import EnderecoSerializer
from ..models import Endereco
from ..services import ViaCEPService


class EnderecoViewSet(viewsets.ModelViewSet):
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()

    def create(self, request, *args, **kwargs):
        cep_param = request.data.get('cep')

        if not cep_param:
            return Response(
                {"error": "O cep é obrigatório."}, status=status.HTTP_400_BAD_REQUEST
            )
        
        dados_cep = ViaCEPService.get_cep(cep_param)

        """isinstance verifica se esse obj e uma instancia de uma classe(na forma nativa do python),
        já nesse contexo, esta verificando se o meu dados_cep esta retornando um dado do tipo string, se for retorna um error e para a execução"""
        if isinstance(dados_cep, str):
            return Response(
                {"error": dados_cep},status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(data=dados_cep)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )