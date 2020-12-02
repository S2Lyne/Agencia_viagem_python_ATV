from Localidade import SSA, FEN, MIA, SYD, BER, DXB
from Voo import Voo, Escala
from Agencia import Agencia
from Reserva import Reserva

class Gerenciador:

    # Gerenciador implementa o padrão Singleton - apenas um é permitido
    _instancia = None
    voos_disponiveis = []

    @staticmethod
    def get_instance():
        if Gerenciador._instancia is None:
            Gerenciador._instancia = Gerenciador()
        return Gerenciador._instancia

    def __init__(self):
        self.ag = Agencia('Agência Nuvem Voadora')
        self.voos_disponiveis.append(Voo(SSA(), BER()))
        self.voos_disponiveis.append(Escala(SSA(), BER(), FEN()))
        self.voos_disponiveis.append(Voo(MIA(), SYD()))
        self.voos_disponiveis.append(Escala(MIA(), SYD(), BER(), DXB()))

    def reservar(self, voo: int, classe):
        print('N° da Reserva: ' + str(self.ag.realizar_reserva(Reserva(self.voos_disponiveis[voo-1], classe)))+'\n')

    def obter_dados_reserva(self, num_reserva):
        print(self.ag.buscar_reserva(num_reserva) + '\n')
