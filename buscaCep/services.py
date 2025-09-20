import requests, types
#com o request podemos enviar solicitações para web
class ViaCEPService:
    """
    com esse decorator não precisamos instanciar a classe para usar a função.
    Podemos chamar a partir da classe
    """
    @staticmethod
    def get_cep(cep: str):
        """
        vamos receber o cep e passar a informação para url
        e nossa resposta vai ser o retorno da request da consulta da url
        se tiver algum erro a raise_for_status() vai lançar uma exception
        """
        url = f"https://viacep.com.br/ws/{cep}/json/"

        try:
            response = requests.get(url)
            """o rase já faz a verificação dos status entre 400 e 600"""
            response.raise_for_status()
            dados_cep = response.json()
            """os dados que vem em forma de strings, quando uso a função .json() ele faz a conversão para o dic/py"""

            if dados_cep.get('erro'):
                return None
            #if "erro" in dados_cep:
            """**dados_cep sendo passado como parametro dessa função vai desempacotar o dicionario python e vai instacializar as chaves para criar instancias para que o getattr possa trabalhar melhor"""
            dados_p_obj = types.SimpleNamespace(**dados_cep)

            response_default = 'Não informado'

            dados_cep_tratados ={
                'cep': getattr(dados_p_obj, 'cep', response_default),
                'logradouro': getattr(dados_p_obj, 'logradouro', response_default),
                'complemento': getattr(dados_p_obj, 'complemento', response_default),
                'bairro': getattr(dados_p_obj, 'bairro', response_default),
                'localidade': getattr(dados_p_obj, 'localidade', response_default),
                'uf': getattr(dados_p_obj, 'uf', response_default),
                'regiao': getattr(dados_p_obj, 'regiao', response_default),
                'ddd': getattr(dados_p_obj, 'ddd', response_default)
            }
            
            return dados_cep_tratados
        
        except requests.exceptions.RequestException as e:
            print(f"ERRO AO ACESSAR O SISTEMA VIACEP: {e}")
            return None

        

