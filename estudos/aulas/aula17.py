class CapacidadeExcedidaError(Exception):
    pass
class HorarioInvalidoError(Exception):
    pass
class SalaIndisponivelErroe(Exception):
    pass

class Sala:
    def __init__(self,nome,capacidade,hora_abertura,hora_fechamento,reservas):
        self.nome = nome
        self.capacidade = capacidade
        self.hora_abertura = hora_abertura
        self.hora_fechamento = hora_fechamento
        self.reservas = reservas

    def pode_reservar(self,inicio,fim):
        if not (self.hora_abertura <= inicio <fim <= self.hora_fechamento):
            raise HorarioInvalidoError("Horario fora do funcionamento da sala")
        if (self.reservas == inicio and fim ):
            raise CapacidadeExcedidaError("Capacidade cheia")
        
Hospital =
        