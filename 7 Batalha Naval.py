from os import system
from random import randint
from time import sleep
x1=6
x2=6
BARCOR=[[2,'32'], [3,'33'], [4,'34'], [5,'35']]
def lin():
    print('='*60)
def linf():
    print('-'*60)
def msg(frase):
    lin()
    print('{:^60}'.format(frase))
    lin()
def conf():
    for cont in range(0, x1):
        for cont2 in range(0, x2):
            TAB1[cont].append(0)
            TAB2[cont].append(0)
            TAB1V[cont].append(0)
            TAB2V[cont].append(0)
            TABMAQ[cont].append(0)
def printtab(TAB, msg='Seu tabuleiro'):
   
    print('{:^60}'.format(msg))
    linf()
    for cont in range(0, x1):
        for cont2 in range(0, x2):
            for cont3 in range(0, len(BARCOR)):
                cor=''
                if TAB[cont][cont2]== BARCOR[cont3][0]:
                    cor=BARCOR[cont3][1]
                    break
            if TAB[cont][cont2]=='x':
                cor='31'
            print(F'\033[{cor}m{TAB[cont][cont2]}\033[m',end='\t')
            if cont2==x2-1:
                print("\n")
def coordenadas():
    while(True):
        try:
            print('Digite as coordenadas iniciais:')
            x=int(input('X = '))
            y=int(input('Y = '))
        except:
            print('\033[31mAs coordenadas devem ser números!\033[m')
            continue
        if -1<x<x1 and -1<y<x2:
            break
        print('\033[31mCoordenadas fora do tabuleiro! Tente novamente\033[m')                  
    return x, y
def monTab(pl, TAB):
 
    msg(f'MONTAGEM DO TABULEIRO DE {pl}')
    printtab(TAB)
    # RODANDO BARCOS'                                  
    for cont in range(0, len(BARC)):
        # COLOCANCO A QUANTIDADE DE CADA BARCO'
        for cont2 in range(0, QUANT[cont]):
            msg(F'Inserir {NOM[cont]}')
            pode=False
 
            # VAI REPETIR ATÉ OS DADOS SEREM COERENTES'
            while pode==False:
                pode=True
                x, y=coordenadas()
                print('Digite a direção do barco')
                cond=input('A - Esquerda\tD - Direita\tS - Baixo\tW - Cima:').upper()
 
                # VENDO SE PODE COLOCAR NO LADO ESCOLHIDO'
                if cond=='D':
                    for cont3 in range(x, x+BARC[cont]):
                        try:
                            if TAB[y][cont3]!=0:
                                print('\033[31mHouve um confronto de posição com outro barco Tente novamente\033[m')
                                pode=False
                        except IndexError:
                            print('\033[31mBarco excededo os limites do tabuleiro!\033[m')
                            pode=False
 
                if cond=='A':
                    for cont3 in range(x-BARC[cont]+1, x+1):
                        if cont3>-1:
                            try:
                                if TAB[y][cont3]!=0:
                                    print('\033[31mHouve um confronto de posição com outro barco Tente novamente\033[m')
                                    pode=False
                            except IndexError:
                                print('\033[31mBarco excededo os limites do tabuleiro!\033[m')
                                pode=False
                        else:
                            print('\033[31mBarco excededo os limites do tabuleiro!\033[m')
                            pode=False
 
                if cond=='W':
                    for cont3 in range(y-BARC[cont]+1, y+1):
                        try:
                            if TAB[cont3][x]!=0:
                                print('\033[31mHouve um confronto de posição com outro barco Tente novamente\033[m')
                                pode=False
                        except IndexError:
                            print('\033[31mBarco excededo os limites do tabuleiro!\033[m')
                            pode=False
 
                if cond=='S':
                    for cont3 in range(y, y+BARC[cont]):
                        try:
                            if TAB[cont3][x]!=0:
                                print('\033[31mHouve um confronto de posição com outro barco Tente novamente\033[m')
                                pode=False
                        except IndexError:
                            print('\033[31mBarco excededo os limites do tabuleiro!\033[m')
                            pode=False
 
            # COLOCANDO'
            
            if cond=='D':
                for cont3 in range(x, x+BARC[cont]):
                    TAB[y][cont3]=BARC[cont]
            if cond=='A':
                for cont3 in range(x-BARC[cont]+1, x+1):
                    TAB[y][cont3]=BARC[cont]
            if cond=='W':
                for cont3 in range(y-BARC[cont]+1, y+1):
                    TAB[cont3][x]=BARC[cont]
            if cond=='S':
                for cont3 in range(y, y+BARC[cont]):
                    TAB[cont3][x]=BARC[cont]
            system('cls') or None
            printtab(TAB)
def jogar(pl, TAB, TABV):
    print('{:^60}'.format(pl + ' joga'))
    while(True):
        x,y=coordenadas()
        if TABV[y][x]!=0:
            print('\033[31mCoordenadas já atingida! Tente novamente\033[m')
        else:
            break
                
    # SE TIVER ALGUM BARCO NESSA POSIÇÃO'   
    if TAB[y][x]!=0:
        # O TABULEIRO VISIVEL RECEBERÁ O VALOR DO QUE FOI ACERTADO NO TABULEIRO REAL'
        TABV[y][x]=TAB[y][x]
        return True
    else:
        TABV[y][x]='x'
        return False
def verificaFim(total, pl, TAB, TABV):
    conta=0
    for cont in range(0, x1):
        for cont2 in range(0, x2):
            if(TAB[cont][cont2]!=0 and TAB[cont][cont2] == TABV[cont][cont2]):
                conta+=1
    if conta==total:
        msg(F'Jogador {pl} ganhou!!!')
        return True
    return False
def monMaq(TAB):
    # CALCULANDO QUANTIDADE DE CASAS PREENCHIDAS'
    for cont in range(0, len(BARC)):
        # COLOCANCO A QUANTIDADE DE CADA BARCO'
        for cont2 in range(0, QUANT[cont]):
            pode=False
            while pode==False:
                pode=True
                letra=randint(0, 3)
                cond=''
               
                if letra==0:
                    cond='D'
                if letra==1:
                    cond='A'
                if letra==2:
                    cond='W'
                if letra==3:
                    cond='S'
                x=randint(0,x1-1)
                y=randint(0,x2-1)
 
                if cond=='D':
                    for cont3 in range(x, x+BARC[cont]):
                        try:
                            if TAB[y][cont3]!=0:
                                pode=False
                        except IndexError:
                                pode=False
                if cond=='A':
                    for cont3 in range(x-BARC[cont]+1, x+1):
                        if cont3>-1:
                            try:
                                if TAB[y][cont3]!=0:
                                    pode=False
                            except IndexError:
                                pode=False
                        else:
                            pode=False
                if cond=='W':
                    for cont3 in range(y-BARC[cont]+1, y+1):
                        try:
                            if TAB[cont3][x]!=0:
                                pode=False
                        except IndexError:
                            pode=False
 
                if cond=='S':
                    for cont3 in range(y, y+BARC[cont]):
                        try:
                            if TAB[cont3][x]!=0:
                                pode=False
                        except IndexError:
                            pode=False
 
            # COLOCANDO'
            if cond=='D':
                for cont3 in range(x, x+BARC[cont]):
                    TAB[y][cont3]=BARC[cont]
            if cond=='A':
                for cont3 in range(x-BARC[cont]+1, x+1):
                    TAB[y][cont3]=BARC[cont]
            if cond=='W':
                for cont3 in range(y-BARC[cont]+1, y+1):
                    TAB[cont3][x]=BARC[cont]
            if cond=='S':
                for cont3 in range(y, y+BARC[cont]):
                    TAB[cont3][x]=BARC[cont]
def verQuedaEmb(TAB, TABMAQ):
    for cont in range(0, x1):
        for cont2 in range(0, x2):
            # Se encontrar um 7            
            if TABMAQ[cont][cont2]==7:

                # Pra direita

                conta=0
                try:
                    TABMAQ[cont][cont2+TAB[cont][cont2]-1]     

                    for cont3 in range(cont2, cont2+TAB[cont][cont2]):
                        if TABMAQ[cont][cont3]==7:
                            conta+=1
                    if conta==TAB[cont][cont2]:
                        for cont3 in range(cont2, cont2+TAB[cont][cont2]):
                            TABMAQ[cont][cont3]=9
                        return 0        
                except IndexError: 1

                # Pra esquerda

                conta=0
                try:
                    TABMAQ[cont][cont2-TAB[cont][cont2]-1]     

                    for cont3 in range(cont2-TAB[cont][cont2], cont2):
                        if TABMAQ[cont][cont3]==7:
                            conta+=1
                    if conta==TAB[cont][cont2]:
                        for cont3 in range(cont2-TAB[cont][cont2], cont2):
                            TABMAQ[cont][cont3]=9
                        return 0        
                except IndexError: 1

                # Pra baixo

                conta=0
                try:
                    TABMAQ[cont+TAB[cont][cont2]-1][cont2]     

                    for cont3 in range(cont, cont+TAB[cont][cont2]):
                        if TABMAQ[cont3][cont2]==7:
                            conta+=1
                    if conta==TAB[cont][cont2]:
                        for cont3 in range(cont, cont+TAB[cont][cont2]):
                            TABMAQ[cont3][cont2]=9
                        return 0
                except IndexError: 1   

                #  Pra cima 

                conta=0
                try:
                    TABMAQ[cont-TAB[cont][cont2]-1][cont2]     

                    for cont3 in range(cont-TAB[cont][cont2], cont):
                        if TABMAQ[cont3][cont2]==7:
                            conta+=1
                    if conta==TAB[cont][cont2]:
                        for cont3 in range(cont-TAB[cont][cont2], cont):
                            TABMAQ[cont3][cont2]=9
                        return 0
                except IndexError: 1
def tiroCego(TAB, TABV, TABMAQ):
    while True:
        x=randint(0, x1-1)
        y=randint(0, x2-1)
        # Se houver algo na posição e não tiver sido atingida
        if TABMAQ[y][x]==0:
            if TAB[y][x]!=0 :
                TABMAQ[y][x]=7
                TABV[y][x]=TAB[y][x]
            else:
                TABMAQ[y][x]=-1
                TABV[y][x]='x'
            return 0
def tiroLateral(TAB, TABV, TABMAQ):
# Sorteando qual será o lado esolhido pra atacar
    for cont in range(0, x1):
        for cont2 in range(0, x2):
        # Se encontrar um 7                
            if TABMAQ[cont][cont2]==7:
                while True:
                    letra = randint(0, 3)
                    if letra==0:
                        cond='D'
                    if letra==1:
                        cond='A'
                    if letra==2:
                        cond='W'
                    if letra==3:
                        cond='S'

                    if cond=='S':
                        # Se exceder o limite
                        try:
                            TABMAQ[cont+1][cont2]
                        except IndexError:
                            continue 
                        # Se essa posição ainda não foi atingida e tem algo ali
                        if TABMAQ[cont+1][cont2]==0:
                            if TAB[cont+1][cont2]!=0:
                                TABMAQ[cont+1][cont2]=7
                                TABV[cont+1][cont2]=TAB[cont+1][cont2]
                            else:
                                TABMAQ[cont+1][cont2]=-1
                                TABV[cont+1][cont2]='x'
                            return True
                        else:
                            continue


                    if cond=='W':
                        # Se exceder o limite
                        try:
                            TABMAQ[cont-1][cont2]
                        except IndexError:
                            continue 
                        # Se essa posição ainda não foi atingida e tem algo ali
                        if TABMAQ[cont-1][cont2]==0:
                            if TAB[cont-1][cont2]!=0:
                                TABMAQ[cont-1][cont2]=7
                                TABV[cont-1][cont2]=TAB[cont-1][cont2]
                            else:
                                TABMAQ[cont-1][cont2]=-1
                                TABV[cont-1][cont2]='x'
                            return True
                        else:
                            continue

                    if cond=='D':
                        # Se exceder o limite
                        try:
                            TABMAQ[cont][cont2+1]
                        except IndexError:
                            continue
                        # Se essa posição ainda não foi atingida e tem algo ali
                        if TABMAQ[cont][cont2+1]==0:
                            if TAB[cont][cont2+1]!=0:
                                TABMAQ[cont][cont2+1]=7
                                TABV[cont][cont2+1]=TAB[cont][cont2+1]
                            else:
                                TABMAQ[cont][cont2+1]=-1
                                TABV[cont][cont2+1]='x'
                            return True
                        else:
                            continue


                    if cond=='A':
                        if cont2-1>-1:
                            # Se exceder o limite
                            try:
                                TABMAQ[cont][cont2-1]
                            except IndexError:
                                continue 
                            # Se essa posição ainda não foi atingida e tem algo ali
                            if TABMAQ[cont][cont2-1]==0:
                                if TAB[cont][cont2-1]!=0:
                                    TABMAQ[cont][cont2-1]=7
                                    TABV[cont][cont2-1]=TAB[cont][cont2-1]
                                else:
                                    TABMAQ[cont][cont2-1]=-1
                                    TABV[cont][cont2-1]='x'
                                return True
                            else:
                                continue                     
def acerto(TAB, TABV, TABMAQ, cont, cont2):
    if TABMAQ[cont][cont2]==0:
        # E tiver acertado
        if TAB[cont][cont2]!=0:
            TABMAQ[cont][cont2]=7
            TABV[cont][cont2]=TAB[cont][cont2]
        # SE tiver errado
        else:
            TABMAQ[cont][cont2]=-1
            TABV[cont][cont2]='x'
        return True
    else:
        return False      
def jogarMaq(TAB, TABV, TABMAQ):
        trava=0
        treco=0
        quant7=0
        
        # Vendo se tem 7
        tem7=False
        for cont in range(0, x1):
            if 7 in TABMAQ[cont]:
                tem7=True

        # Se tiver 7
        if tem7:
            for cont in range(0, x1):
                for cont2 in range(0, x2):
                    # Se encontrar um 7
                    
                    if TABMAQ[cont][cont2]==7:
                            quant7+=1
                    
                    
                            # Analisando a direção do proximo sete se ele existir
                            direcao=''            
                            try:
                                TABMAQ[cont][cont2+2]                     
                                if TABMAQ[cont][cont2+1]==7:
                                    direcao='D'
                                else:
                                    treco+=1
                            except IndexError: treco+=1

                            try:
                                TABMAQ[cont][cont2-2]
                                if TABMAQ[cont][cont2-1]==7 and cont2-2>-1:
                                    direcao='A'
                                else:
                                    treco+=1
                            except IndexError: treco+=1

                            try:
                                TABMAQ[cont-2][cont2]
                                if  TABMAQ[cont-1][cont2]==7:
                                    direcao='W'
                                else:
                                    treco+=1
                            except IndexError: treco+=1

                            try:
                                TABMAQ[cont+2][cont2]
                                if TABMAQ[cont+1][cont2]==7:
                                    direcao='S'
                                else:
                                    treco+=1
                            except IndexError: treco+=1

                            # husuahsa

                            try:
                                TABMAQ[cont][cont2-1]                     
                                if TABMAQ[cont][cont2+1]==7 and cont2-1>-1:
                                    direcao='DP'
                                else:
                                    treco+=1
                            except IndexError: treco+=1

                            try: 
                                TABMAQ[cont][cont2+1]
                                if TABMAQ[cont][cont2-1]==7:
                                    direcao='AP'
                                else:
                                    treco+=1
                            except IndexError: treco+=1

                            try:
                                TABMAQ[cont+1][cont2]
                                if  TABMAQ[cont-1][cont2]==7:
                                    direcao='WP'
                                else:
                                    treco+=1
                            except IndexError: treco+=1
                            try:
                                TABMAQ[cont-1][cont2]
                                if TABMAQ[cont+1][cont2]==7:
                                    direcao='SP'
                                else:
                                    treco+=1
                            except IndexError: treco+=1

                            # Se tiver um 7 a direita
                            if direcao=='D':
                                if acerto(TAB, TABV, TABMAQ, cont, cont2+2):
                                    return 0
                                else:
                                    trava+=1
                            if direcao=='A':
                                if acerto(TAB, TABV, TABMAQ, cont, cont2-2):
                                    return 0
                                else:
                                    trava+=1
                            if direcao=='S':
                                if acerto(TAB, TABV, TABMAQ, cont+2, cont2):
                                    return 0
                                else:
                                    trava+=1
                            if direcao=='W':
                                if acerto(TAB, TABV, TABMAQ, cont-2, cont2):
                                    return 0
                                else:
                                    trava+=1
                                
                            if direcao=='DP':
                                if acerto(TAB, TABV, TABMAQ, cont, cont2-1):
                                    return 0
                                else:
                                    trava+=1
                            if direcao=='AP':
                                if acerto(TAB, TABV, TABMAQ, cont, cont2+1):
                                    return 0
                                else:
                                    trava+=1
                            if direcao=='SP':
                                if acerto(TAB, TABV, TABMAQ, cont-1, cont2):
                                    return 0
                                else:
                                    trava+=1
                            if direcao=='WP':
                                if acerto(TAB, TABV, TABMAQ, cont+1, cont2):
                                    return 0
                                else:
                                    trava+=1

                            quant7=0
                            for cont3 in range(0, x1):
                                for cont4 in range(0, x2):
                                    if TABMAQ[cont3][cont4]==7:
                                        quant7+=1

                            # Se não houver 7 lateral
                            if trava==quant7 or treco==8:
                                tiroLateral(TAB, TABV, TABMAQ)
                                return 0
            
        # Se não tiver 7
        else:
            tiroCego(TAB, TABV, TABMAQ)
def printFinal():
    printtab(TAB2V, 'O tabuleiro inimigo visivel')
    linf()
    printtab(TAB2, 'O tabuleiro inimigo real')
    lin()
    printtab(TAB1V, 'Seu tabuleiro visivel')
    linf()
    printtab(TAB1, 'Seu tabuleiro real')
 

TAB1= [[],[],[],[],[],[],[],[],[],[]]
TAB2= [[],[],[],[],[],[],[],[],[],[]]
TAB1V=[[],[],[],[],[],[],[],[],[],[]]
TAB2V=[[],[],[],[],[],[],[],[],[],[]]
TABMAQ=[[],[],[],[],[],[],[],[],[],[]]
 
conf()
BARC=[2, 3, 4, 5]
NOM= ["Lancha","Cargueiro","Fuzileiro","Porta Aviões"]
QUANT=[3, 2,2,1]
# CALCULANDO QUANTIDADE DE CASAS PREENCHIDAS'
total=0
for cont in range(0,len(BARC)):
    total+=BARC[cont]*QUANT[cont]
 
# MENU'
msg("BATALHA NAVAL")
var=input('1 - PvP\n2 - PvM\n')
# PvP'
if(var==1):
    pl1=input('Digite o nome do primeiro jogador: ')
    pl2=input('Digite o nome do segundo jogador: ')
   
    # MONTAGEM DO TABULEIRO'
 
    monTab(pl1, TAB1)
    system('cls') or None
 
    monTab(pl2, TAB2)
    system('cls') or None
   
    system('cls') or None
    msg('HORA DO JOGO')
   
   
    while True:
        # PLAYER 1 JOGA'
        jogar(pl1, TAB2, TAB2V)
        if verificaFim(total, pl1, TAB2, TAB2V):
            break
 
        # PLAYER 2 JOGA'
        jogar(pl2, TAB1, TAB1V)
        if verificaFim(total, pl2, TAB1, TAB1V):
            break
 
else:
    pl1=input('Digite o nome do primeiro jogador: ')
 
    # MONTAGEM DO TABULEIRO'
    monTab(pl1, TAB1)
    system('cls') or None

    monMaq(TAB2)
     
    msg('HORA DO JOGO')

    while True:
        
        printtab(TAB2V, 'O tabuleiro do inimigo conhecido')
        var = jogar(pl1, TAB2, TAB2V)
        if var:    
            print('{:^60}'.format('\033[33mVocê acertou!!!\033[m'))
        else:
            print('{:^60}'.format('\033[31mVocê errou!!!\033[m'))
        linf()

        input('De enter para continuar')
        system('cls') or None
        # Máquina Joga
        jogarMaq(TAB1, TAB1V, TABMAQ)
        verQuedaEmb(TAB1, TABMAQ)
        # 
        printtab(TAB1V)
        input('De enter para continuar')
        system('cls') or None

        if verificaFim(total, pl1, TAB2, TAB2V):
            printFinal()
            break
        if verificaFim(total, 'Máquina', TAB1, TAB1V):
            printFinal()
            break
            
            




   
   
 
 
 
   
 
 
 
