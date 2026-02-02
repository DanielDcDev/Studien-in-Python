from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def mensagem(self, mensagem):
        pass

class Email(Notificacao):
    def enviar(self,mensagem):
        print("Email enviado{mensagem}")
class SMS(Notificacao):
    def enviar(self,mensagem):
        print(f"SMS enviado: {mensagem}")
        