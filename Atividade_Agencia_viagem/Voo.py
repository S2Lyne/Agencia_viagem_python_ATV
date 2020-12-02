from Localidade import Localidade, SSA, FEN, MIA, SYD, BER, DXB

class Voo:

    '''Uso do Padão de projeto Decorator '''
    num_voo = 230

    def __init__(self, origem: Localidade, destino: Localidade):
        self.origem = origem
        self.destino = destino
        self.escalas = []
        self.n_voo = Voo.num_voo
        Voo.num_voo += 1

    def get_taxa(self):

        taxa = self.origem.taxa_aeroporto + self.destino.taxa_aeroporto

        for esc in self.escalas:
            taxa += esc.taxa_aeroporto
        return taxa

    def get_info_voo(self):
        info = 'N° Vôo: '+ str(self.n_voo) + '\n' + 'Origem: ' + self.origem.nome + '| Destino: ' + self.destino.nome + '| Escala:' 
        for esc in self.escalas:
            info += esc.nome + ','
     
        return info

class Escala(Voo):
    def __init__(self, origem: Localidade, destino: Localidade, *escalas):
        super().__init__(origem, destino)
        self.escalas = escalas







    


