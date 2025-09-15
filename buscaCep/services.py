import requests
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
            response.raise_for_status()
            dados_cep = response.json()

            if "erro" in dados_cep:
                return None
            
            return dados_cep
        
        except requests.exceptions:
            return None

        

