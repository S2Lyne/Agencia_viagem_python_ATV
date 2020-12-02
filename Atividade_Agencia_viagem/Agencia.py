from Reserva import Reserva

class Agencia:

    _list_reservas = []

    def __init__(self, nome):
        self.nome = nome

    @staticmethod
    def realizar_reserva(reserva: Reserva):
        Agencia._list_reservas.append(reserva)

        return reserva.get_num_reserva

    def buscar_reserva(self, num_reserva):
        result= ''
        achou = False
        for res in Agencia._list_reservas:
            if int(num_reserva) == int(res.get_num_reserva):
                result = res.get_info_reserva()
                achou = True
        if achou:
            return result
        else:
            print('Reserva não encontrada')   

