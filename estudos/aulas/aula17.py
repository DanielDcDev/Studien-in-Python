class CapacidadeExcedidaError(Exception):
    pass
class HorarioInvalidoError(Exception):
    pass
class SalaIndisponivelError(Exception):
    pass

class Sala:
    def __init__(self,nome,hora_abertura,hora_fechamento,capacidade):
        self.nome = nome
        self.hora_abertura = hora_abertura
        self.hora_fechamento = hora_fechamento
        self.capacidade = capacidade

    def pode_reservar(self,inicio,fim, pessoas):
        if not (self.hora_abertura <= inicio < fim <= self.hora_fechamento):
            raise HorarioInvalidoError("Horario fora do funcionamento da sala")
        if (pessoas > self.capacidade):
            raise CapacidadeExcedidaError("Capacidade cheia")
        
        return True

class Reserva:
    reservas  = []
    def __init__(self,responsavel,inicio,fim,pessoas):
        self.responsavel = responsavel
        self.inicio = inicio
        self.fim = fim
        self.pessoas = pessoas
    
    def validar_horario(self,horario_inicio, horario_termino, pessoas):
        if  self.inicio <= horario_inicio < horario_termino <= self.fim and  self.pessoas <= pessoas  and Sala.capacidade <= pessoas:
            return print("A sua reserva pode ser feita")
        else:
            raise HorarioInvalidoError("horario e/ou capacidade invalido")
        

    
        
hospital = Sala("Casa Limpeza", 8, 19, 10,)
ReservaDaniel = Reserva("Carlos", 8,19,9)  
try:
    hospital.pode_reservar(17, 18, 5)
    print("Reserva permitida")
except Exception as e:
    print(e)

ReservaDaniel.validar_horario(9,10,8)

        