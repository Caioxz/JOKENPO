import random
from colorama import Fore, Back, Style, init
from time import sleep

itens_PPT = ['Pedra','Papel','Tesoura✂']
bot = random.randint(0,2)
print( Fore.LIGHTWHITE_EX+'''Suas opções:
[0] PEDRA
[1] TESOURA
[2] PAPEL''')

jogador = int(input('Qual vai ser a sua jogada?'))

print(Fore.LIGHTRED_EX+'JO')
sleep(1)
print(Fore.LIGHTBLUE_EX+'KEN')
sleep(1.5)
print(Fore.LIGHTCYAN_EX+'PO!!')
sleep(1.7)
print(Fore.LIGHTWHITE_EX+'-=' *11)
print(Fore.LIGHTWHITE_EX+'Jogador: '+ Fore.LIGHTGREEN_EX+'{}'.format(itens_PPT[jogador]))
print(Fore.LIGHTWHITE_EX+'Computador: '+ Fore.LIGHTGREEN_EX+'{}'.format(itens_PPT[bot]))
print(Fore.LIGHTWHITE_EX+'-=' *11)

if bot == 0:
    if jogador == 0:
        print(Fore.LIGHTBLUE_EX+'EMPATE')
    elif jogador == 1:
        print(Fore.LIGHTGREEN_EX+'JOGADOR VENCEU')
    elif jogador == 2:
        print(Fore.LIGHTRED_EX+'COMPUTADOR VENCEU')
    else:
        print(Fore.LIGHTRED_EX+'JOGO INVALIDO!!')

if bot == 1:
    if jogador == 0:
        print(Fore.LIGHTGREEN_EX+'JOGADOR VENCEU')
    elif jogador == 1:
        print(Fore.LIGHTBLUE_EX + 'EMPATE')
    elif jogador == 2:
        print(Fore.LIGHTGREEN_EX+'COMPUTADOR VENCEU')
    else:
        print(Fore.LIGHTRED_EX+'JOGO INVALIDO!!')

if bot == 2:
    if jogador == 0:
        print(Fore.LIGHTGREEN_EX + 'COMPUTADOR VENCEU')
    elif jogador == 1:
        print(Fore.LIGHTGREEN_EX+'JOGADOR VENCEU')
    elif jogador == 2:
        print(Fore.LIGHTBLUE_EX + 'EMPATE')
    else:
        print(Fore.LIGHTRED_EX+'JOGO INVALIDO!!')
