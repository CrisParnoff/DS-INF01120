from fastapi import APIRouter
from BackEnd.Dtos.interface_dto import InterfaceDTO

router = APIRouter()

@router.post("/enviar-form")
async def receber_dados(dados: InterfaceDTO):
    try:
        # No futuro, é aqui que você vai chamar o seu controller
        # resultado = controller.processar_dados(dados)
        
        # Por enquanto, apenas retornamos o que chegou para testar a rota
        return {"status": "sucesso", "valor_recebido": dados.texto}
        
    except Exception as e:
        # A rota captura qualquer erro e devolve um Status 500 (Internal Server Error) padrão
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro interno ao processar a requisição: {str(e)}"
        )