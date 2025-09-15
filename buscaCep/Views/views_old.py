from ..models import Endereco
from ..serializers import EnderecoSerializers
from ..services import ViaCEPService
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view 

"""lembrando que o request tem todas as informações da requisição
request.mothod, request.user, request.data e mesmo que não seja usado é obrigatório ter
"""
@api_view(['GET'])
def consultar_cep(request, cep_param: str):
    cep = cep_param.replace('-','').replace('.','')
    infoNotFaund = "Não localizado"
    try:
        search_cep = Endereco.objects.exists(cep=cep)

        if search_cep:
            local_cep = Endereco.objects.get(cep=cep)
            serializer = EnderecoSerializers(local_cep)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return f"Buscando endereço da api externa"
    except Endereco.DoesNotExist:
        external_cep = ViaCEPService.get_cep(cep)

        if not 'erro':
            new_cep = Endereco.objects.create(
                cep = external_cep.get('cep',infoNotFaund),
                logradouro = external_cep.get('logradouro', infoNotFaund),
                complemento=external_cep.get('complemento', infoNotFaund ),
                bairro=external_cep.get('bairro', infoNotFaund),
                localidade=external_cep.get('localidade', infoNotFaund),
                uf=external_cep.get('uf', infoNotFaund),
                regiao = external_cep.get('regiao', infoNotFaund),
                ddd = external_cep.get('ddd', infoNotFaund)
            )

            serializer = EnderecoSerializers(new_cep)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"CEP informado não existe na base de dados"},
                status=status.HTTP_404_NOT_FOUND
            )

