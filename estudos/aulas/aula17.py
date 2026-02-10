class CapacidadeExcedidaError(Exception):
    pass
class HorarioInvalidoError(Exception):
    pass
class SalaIndisponivelErroe(Exception):
    pass

class Sala:
    def __init__(self,nome,hora_abertura,hora_fechamento,reservas):
        self.nome = nome
        self.hora_abertura = hora_abertura
        self.hora_fechamento = hora_fechamento
        self.reservas = reservas
        self.capacidade = 10

    def pode_reservar(self,inicio,fim):
        if not (self.hora_abertura <= inicio <fim <= self.hora_fechamento):
            raise HorarioInvalidoError("Horario fora do funcionamento da sala")
        else :
            print("Parabens voce foi selecionado")
        if (self.capacidade < self.reservas):
            raise CapacidadeExcedidaError("Capacidade cheia")
        else:
            print("Parabens voce foi selecionado")

        
Hospital =Sala("Casa Limpeza", 8, 19,12)

Hospital.pode_reservar(18,19)

        