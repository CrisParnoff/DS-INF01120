from Dtos.interface_obj import InterfaceDTO
from Services.music_service import MusicService

class InterfaceController:
    def __init__(self):
        self.music_service = MusicService()

    def processar_dados(self, dados: InterfaceDTO) -> dict:
        try:
            texto_recebido = dados.texto
            
            if not texto_recebido:
                raise ValueError("O texto enviado não pode estar vazio.")
            
            # 1. Traduz o texto para a partitura (Lista de dicionários)
            sequencia_musical = self.music_service.gerar_sequencia(texto_recebido)
            
            # 2. Devolve o JSON pronto para o navegador tocar
            return {
                "status": "sucesso", 
                "total_eventos": len(sequencia_musical),
                "sequencia": sequencia_musical
            }
            
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro inesperado: {str(e)}")