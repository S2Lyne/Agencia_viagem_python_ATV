from Voo import Voo

class Reserva:

    _num_reserva = 1000

    def __init__(self, voo: Voo, classe = 'X'):
        self.voo = voo
        self.classe = classe
        self.n_reserva = Reserva._num_reserva
        Reserva._num_reserva += 1

    def get_preco_final(self):
        preco_final = 0.00

        if self.classe == 'X':
            preco_final = self.voo.get_taxa() + 200
        else:
            preco_final = self.voo.get_taxa()
        return preco_final
        
    @property
    def get_num_reserva(self):
        return self.n_reserva

    def get_info_reserva(self):
        info =  self.voo.get_info_voo()

        if self.classe == 'X':
            info += 'Classe Executiva \n'

        else:
            info += 'Classe Econômica \n'
        
        info += 'Preço (R$): ' + str(self.get_preco_final())

        return info