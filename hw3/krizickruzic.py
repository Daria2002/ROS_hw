def ispisPolja(polje):
    '''ispisuje polje'''
    print('The Tic-tac-toe game')
    print('********************')
    for el in polje:
        print(el)
          
def provjeriPoziciju(red, stupac, polje):
    '''provjerava jesu li red i stupac dopuštenih dimenzija i je li se na zeljenom mjestu postavljanja znaka već
    nalazi neki znak. Ukoliko je sve ok sa zadanom pozicijom vraća 0, a ako je pozicija krivo zadana vraća 1'''

    #provjeravanje dimenzija
    if(red < 1 or red>3 or stupac<1 or stupac>3):
        print('Red i stupac trebaju biti cijeli broj u intervalu 1-3')
        return 1
    #provjeravanje zauzetosti elementa u polju
    elif(polje[red-1][stupac-1]=='x' or polje[red-1][stupac-1]=='o'):
        print('na tom mjestu se vec nalazi {0}'.format(polje[red-1][stupac-1]))
        return 1
    else:
        return 0
 
def iniPolje(polje):
    '''inicijalizira elemente polja na -1'''
    polje = [[-1 for m in range(3)] for n in range(3)]   
    return polje

def krajIgre(polje):
    '''provjerava jesu li sva polja ispunjena i je li igra zavrsila bez pobjednika'''
    for i in range(0, 3):
        for j in range(0, 3):
            if(polje[i][j]==-1):
                return 0
    return 1

def netkoJePobjedio(polje, znak):
    '''provjerava je li x ili o pobjedio'''

    #provjeravanje pobjede u retcima i stupcima
    for i in range(0, 3):
        if(polje[0][i]==polje[1][i]==polje[2][i] and (polje[0][i]=='o' or polje[0][i]=='x')):
            return  1
        if(polje[i][0]==polje[i][1]==polje[i][2] and (polje[i][0]=='o' or polje[i][0]=='x')):
            return 1

    #provjeravanje diagonale1
    if(polje[0][0]==polje[1][1]==polje[2][2] and (polje[0][0]=='x' or polje[0][0]=='o')):
        return 1

    #provjeravanje diagonale2
    elif (polje[0][2] == polje[1][1] == polje[2][0] and (polje[0][2] == 'x' or polje[0][2] == 'o')):
        return 1
    return 0

novaIgra = 'y'

while(novaIgra=='y'):
    polje=[]
    polje = iniPolje(polje)

    for k in range (1,10):
        #ispisivanje polja nakon svakog unosa znaka
        ispisPolja(polje)

        #postavljanje znaka na vrijednost koja se postavlja
        if (k%2==1):
            znak = 'x'
        else:
            znak = 'o'

        while (True):
            krivaPozicija = 0
            try:
                #unos pozicije
                red, stupac = eval(input('{0}: unesite broj zeljenog reda i stupaca(odvojiti zarezom):'.format(znak)))
                if(provjeriPoziciju(red, stupac, polje)):
                    krivaPozicija = 1
                    raise NameError
                break
            except Exception:
                if(krivaPozicija==0):
                    print('Pozicija koju ste zadali je pogrešna. Upute za unos željene pozicije:\
red i stupac su cijeli brojevi, a potrebno ih je odvojiti zarezom.')

        #postavljanje znaka na polje
        polje[red - 1][stupac - 1] = znak

        #provjeravanje pobjednika
        if(netkoJePobjedio(polje,znak)):
            print('{0} je pobjedio'.format(znak))
            break

        #provjeravanje kraja igre
        if(krajIgre(polje)):
            print('u ovoj igri nema pobjednika')
            break

    novaIgra = input('zelite li novu igru? y \ n ')

