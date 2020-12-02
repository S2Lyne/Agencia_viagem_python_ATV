from OpcaoInvalidaError import OpcaoInvalidaError
from Gerenciador import Gerenciador

def main():
    ger = Gerenciador()
    opcao = -1
    while opcao != 3:
        print("=============== *-* Agência Nuvem Voadora *-* ===============")
        try:
            opcao = int(input('''
            Olá o que deseja fazer na Agência Nuvem Voadora?
            1) Reservar Vôo
            2) Ver dados da reserva
            3) Sair\n'''))
        except ValueError:
            print("Informe apenas um número.")
        else:
            if 0 < opcao < 2 :
                escolher_acao(opcao)
            elif opcao == 2:
                dados_reserva()
            elif opcao == 3:
                break
            elif opcao > 3:
                print("Informe um número válido.")


def escolher_acao(acao): 
    try:
        escolha = int(input('''Escolha o escolha Vôo:
        1) SSA - BER (Direto)
        2) SSA - BER (Escala em FEN)
        3) MIA - SYD (Direto)
        4) MIA - SYD (Escala em BER e DXB) \n'''))

        if escolha < 1 and escolha > 5:
            raise OpcaoInvalidaError()
    except ValueError:
        print(OpcaoInvalidaError.mensagem_padrao)
    else:
        escolher_classe(escolha)



def escolher_classe(escolha):
        ger = Gerenciador()
        classe = input('''Escolha a Classe que deseja viajar:
        X -  Classe Executiva
        Outra tecla - Classe Econômica \n''')
        
        return ger.reservar(escolha, classe)

def dados_reserva():
    ger = Gerenciador()
    return ger.obter_dados_reserva(input('Informe o Número da reserva \n'))
    

main()