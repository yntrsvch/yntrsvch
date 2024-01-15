import datetime
import random
import sys
import os
from time import sleep

plansza = ["_","_","_","_","_","_"," "," "," "]
ktoryRuch = 1
rogi = [0,2,6,8]
boki = [1,3,5,7]
mozliweRzedyWygrania = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


print("Zagrajmy w kółko i krzyżyk!")
print("O to indeksy na planszy:")
print("1|2|3")
print("4|5|6")
print("7|8|9\n")
print("Zaczynasz grę.")
sleep(4)


def drukujPlansze(plansza, ktoryRuch):
    os.system("cls")
    print (plansza[0]+ "|" +plansza[1] + "|" + plansza[2])
    print (plansza[3]+ "|" +plansza[4] + "|" + plansza[5])
    print (plansza[6]+ "|" +plansza[7] + "|" + plansza[8])

    ruchGracza(plansza, ktoryRuch)


def ruchGracza(plansza, ktoryRuch):

    index = input("Wybierz indeks gdzie chcesz postawić 'O': ")
    
    if index.isdigit():
        index = int(index) - 1
        if int(index)>8 or int(index)<0:
            print("Musisz wybrać numer z zakresu 1-9")
            ruchGracza(plansza, ktoryRuch)

        if(plansza[int(index)]=="X" or plansza[int(index)]=="O"):
            print("To miejsce jest już zajęte")
            ruchGracza(plansza, ktoryRuch)
            
        else:
            plansza[int(index)] = "O"

        if(czyKtosWygral(plansza, mozliweRzedyWygrania)==True):
            zakonczenie(plansza)
        else:
            
            ruchKomputera(plansza, rogi, boki, ktoryRuch, mozliweRzedyWygrania)
    else:
        print("Musisz wpisać liczbę całkowitą")
        ruchGracza(plansza, ktoryRuch)
    

def ruchKomputera(plansza, rogi, boki, ktoryRuch, mozliweRzedyWygrania):
    wykonanyRuch = False

    def wyborRogu(rogi, plansza):
        mozliweWybory = []
        for i in rogi:
            if (plansza[i]==" " or plansza[i]=="_"):
                mozliweWybory.append(i)
        k = random.choice(mozliweWybory)
        plansza[k]="X"  

    def wyborBoku(boki, plansza):
        mozliweWybory = []
        for i in boki:
            if (plansza[i]==" " or plansza[i]=="_"):
                mozliweWybory.append(i)

        if mozliweWybory==[]:
            wyborRogu(rogi, plansza)
            
        else:
            plansza[random.choice(mozliweWybory)]="X"
    

    #sprawdzenie czy środek jest wolny w 1 kolejce
    if ktoryRuch==1:
        if (plansza[4]==" " or plansza[4]=="_"):
            #wybór środka
            plansza[4]="X"
            ktoryRuch += 1
            wykonanyRuch = True
        else: 
            #randomowy róg
            wyborRogu(rogi, plansza)
            ktoryRuch += 1
            wykonanyRuch = True
            

    else:
        if wykonanyRuch==False:
            #wygranie komputera
            for i in mozliweRzedyWygrania:
                if(plansza[i[0]]=="X" and plansza[i[1]]=="X" 
                and (plansza[i[2]]==" " or plansza[i[2]]=="_")):
                    plansza[i[2]]="X"
                    ktoryRuch += 1
                    wykonanyRuch = True
                    break
                if wykonanyRuch==False:
                    if(plansza[i[0]]=="X" and (plansza[i[1]]==" "
                    or plansza[i[1]]=="_") and plansza[i[2]]=="X"):
                        plansza[i[1]]="X"
                        ktoryRuch += 1
                        wykonanyRuch = True
                        break
                if wykonanyRuch==False:
                    if((plansza[i[0]]==" " or plansza[i[0]]=="_") 
                    and plansza[i[1]]=="X" and plansza[i[2]]=="X"):
                        plansza[i[0]]="X"
                        ktoryRuch += 1
                        wykonanyRuch = True
                        break


            #blokowanie
            if wykonanyRuch==False:
                for i in mozliweRzedyWygrania:
                    if(plansza[i[0]]=="O" and plansza[i[1]]=="O" 
                    and (plansza[i[2]]==" " or plansza[i[2]]=="_")):
                        plansza[i[2]]="X"
                        ktoryRuch += 1
                        wykonanyRuch = True
                        break
                    if wykonanyRuch==False:
                        if(plansza[i[0]]=="O" and (plansza[i[1]]==" "
                        or plansza[i[1]]=="_") and plansza[i[2]]=="O"):
                            plansza[i[1]]="X"
                            ktoryRuch += 1
                            wykonanyRuch = True
                            break
                    if wykonanyRuch==False:
                        if((plansza[i[0]]==" " or plansza[i[0]]=="_") 
                        and plansza[i[1]]=="O" and plansza[i[2]]=="O"):
                            plansza[i[0]]="X"
                            ktoryRuch += 1
                            wykonanyRuch = True
                            break

    if wykonanyRuch==False:
        if ktoryRuch==2 and plansza[4]=="X":

            mozliweRzedyBokowWygranej = [[1,4,7],[3,4,5]]
            bokiGracza = 0

            for i in boki:
                if(plansza[i]=="O"):
                    bokiGracza += 1

            #Sytuacje tego typu:
            # O|_|_ <- tutaj musi być postawiony X
            # _|X|O
            #  | |

            # _|_|_ 
            # O|X|
            #  | |O  <- na pierwszym miejscu musi być postawiony X
            if bokiGracza == 1:
                mozliweRzedyInne = [[0,7],[2,7],[1,8],[1,6],[2,3],[3,8],[0,5],[5,6]]

                if wykonanyRuch==False:
                    for i in mozliweRzedyInne:
                        if(plansza[i[0]]=="O" and plansza[i[1]]=="O"):
                            for j in mozliweRzedyBokowWygranej:
                                if ((plansza[j[0]]==" "or plansza[j[0]]=="_") 
                                and (plansza[j[2]]==" "or plansza[j[2]]=="_")):
                                    #tutaj mogloby byc tez j[2]
                                    #wybor jednego z 2 rzedow bokow gdzie sa 2 wolne miejsca
                                    plansza[j[0]]="X"
                                    ktoryRuch += 1
                                    wykonanyRuch = True

            #  O| |_     _| |O    
            #  _|X|_     _|X|_    
            #  _| |O     O| |_  
            elif bokiGracza == 0:
                #wybiera bok
                wyborBoku(boki, plansza) 
                ktoryRuch += 1
                wykonanyRuch = True 

            else:
                #  _|O|_     _| |_    _| |_
                #  _|X|O     _|X|O    O|X|O
                #  _| |_     _|O|_    _| |_ <- wybiera ten róg
                if plansza[5]=="O":
                    plansza[8]="X"
                    ktoryRuch += 1
                    wykonanyRuch = True

                #  _|O|_     _| |_   
                #  O|X|_     O|X|_   
                #  _| |_  -> _|O|_  wybiera ten róg
                elif plansza[3]=="O":
                    plansza[6]="X"
                    ktoryRuch += 1
                    wykonanyRuch = True

                #  _|O|_  
                #  _|X|_  
                #  _|O|_  
                else:
                    wyborRogu(rogi, plansza)
                    ktoryRuch += 1
                    wykonanyRuch = True
                
        elif ktoryRuch==2 and plansza[4]=="O":
            #randomowy corner
            wyborRogu(rogi, plansza)
            ktoryRuch += 1
            wykonanyRuch = True

        #  O|_|_ <- tu trzeba dać X
        #  X|X|O
        #   |O|

        elif ktoryRuch==3 and plansza[4]=="X":
                noweRzedy = [[0,5,7,3,4],[0,5,6,3,4],[1,5,6,3,4],[2,3,8,4,5],[1,3,8,4,5],[2,3,7,4,5]]

                for i in range(0, len(noweRzedy)):
                    if (plansza[noweRzedy[i][0]]=="O" 
                    and plansza[noweRzedy[i][1]]=="O" 
                    and plansza[noweRzedy[i][2]]=="O" 
                    and plansza[noweRzedy[i][3]]=="X" 
                    and plansza[noweRzedy[i][4]]=="X"):
                        if (i==0):
                            plansza[2]="X"
                            ktoryRuch += 1
                            wykonanyRuch = True
                        
                        elif (i==1 or i==2):
                            plansza[8]="X"
                            ktoryRuch += 1
                            wykonanyRuch = True
                        
                        elif (i==3 or i==5):
                            plansza[0]="X"
                            ktoryRuch += 1
                            wykonanyRuch = True
                    
                        elif (i==4):
                            plansza[6]="X"
                            ktoryRuch += 1
                            wykonanyRuch = True

                if wykonanyRuch==False:
                    bokiGracza = 0
                    for i in boki:
                        if(plansza[i]=="O"):
                            bokiGracza += 1

                    if bokiGracza >= 1:
                        #wybiera corner
                        wyborRogu(rogi, plansza)
                        ktoryRuch += 1
                        wykonanyRuch = True
                    else:
                        #wybiera bok
                        wyborBoku(boki, plansza)
                        ktoryRuch+=1
                        wykonanyRuch = True   

        else:
            bokiGracza = 0
            for i in boki:
                if(plansza[i]=="O"):
                    bokiGracza += 1

            if bokiGracza >= 1:
                #wybiera corner
                wyborRogu(rogi, plansza)
                ktoryRuch += 1
                wykonanyRuch = True
            else:
                #wybiera bok
                wyborBoku(boki, plansza)
                ktoryRuch+=1
                wykonanyRuch = True                       


    if (czyKtosWygral(plansza, mozliweRzedyWygrania)==True):
        zakonczenie(plansza)
    else:
        drukujPlansze(plansza, ktoryRuch)


def czyKtosWygral(plansza, mozliweRzedyWygrania):

    global winner

    for i in mozliweRzedyWygrania:
        if(plansza[i[0]]=="X" and plansza[i[1]]=="X" and plansza[i[2]]=="X"):
            winner = "Komputer"
            return True
        if(plansza[i[0]]=="O" and plansza[i[1]]=="O" and plansza[i[2]]=="O"):
            winner = "Gracz"
            return True

        filled = 0

        for j in range(0, len(plansza)):
            if (plansza[j]!=" " and plansza[j]!="_"):
                filled = filled + 1
            if filled==9:
                winner = "Remis"
                return True
   
    return False


def zakonczenie(plansza):
    print("Ostateczna plansza:")
    print (plansza[0]+ "|" +plansza[1] + "|" + plansza[2])
    print (plansza[3]+ "|" +plansza[4] + "|" + plansza[5])
    print (plansza[6]+ "|" +plansza[7] + "|" + plansza[8])

    if winner=="Remis":
        print("Remis")
    else:
        print("Zwycięzca to: "+ winner)

    iloscRuchowGracza = 0
    for i in range(0,len(plansza)):
        if (plansza[i]=="O"):
            iloscRuchowGracza+=1

    print(f"Gra zakończyła się po wykonaniu {iloscRuchowGracza} ruchów Gracza.")

    plik_wyjsciowy = open("wynik.txt","a")
    plik_wyjsciowy.write(f"\n{winner}\n")
    plik_wyjsciowy.write(datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")+"\n")
    plik_wyjsciowy.write(f"{iloscRuchowGracza}")
    sys.exit(0)


drukujPlansze(plansza, ktoryRuch)
