from abc import ABC, abstractmethod
from models.estado_musical import EstadoMusical
from models.evento_musical import EventoMusical


class RegraBase(ABC):

    @abstractmethod
    def deve_processar(self, char: str, estado: EstadoMusical) -> bool:
        """Retorna True se esta regra se aplica ao caractere dado."""
        ...

    @abstractmethod
    def processar(self, char: str, estado: EstadoMusical) -> EventoMusical | None:
      
        ...
