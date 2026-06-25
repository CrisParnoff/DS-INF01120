from regras.regra_base import RegraBase
from models.estado_musical import EstadoMusical
from models.evento_musical import EventoMusical, TipoEvento

_INSTRUMENTOS = {
    "!":  22,   # Harmonica 
    ";":  15,   # Tubular Bells
    ",":  20,   # Church Organ 
}


class RegraInstrumento(RegraBase):
    """Caracteres especiais trocam o instrumento atual."""

    def deve_processar(self, char: str, estado: EstadoMusical) -> bool:
        return char in _INSTRUMENTOS

    def processar(self, char: str, estado: EstadoMusical) -> EventoMusical:
        novo_instrumento = _INSTRUMENTOS[char]
        estado.trocar_instrumento(novo_instrumento)
        estado.registrar_nao_nota()

        # Para nova linha, envia representação legível no JSON
        char_legivel = "\\n" if char == "\n" else char

        return EventoMusical(
            tipo=TipoEvento.CHANGE_INSTRUMENT,
            char=char_legivel,
            instrumento=estado.instrumento,
        )
