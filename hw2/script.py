#prvi zdk
lista = []
while True:
    
    try:
        num = float(input('Upisite 0 za kraj, ili bilo koji drugi broj drugo za nastavak '))
    except Exception:
        print("Molimo upisite broj.")
        continue

    if num == 0:
        break

    lista.append(num)

suma = sum(lista)

sequenceFile = open('sequence.txt', 'w')
firstElement=True
for element in lista:

    if firstElement:
        sequenceFile.write('{0}'.format(element))
        firstElement = False

    else:
        sequenceFile.write(' {0}'.format(element))

sequenceFile.write(' \n{0}'.format(suma))
sequenceFile.close()

#drugi zdk  
numLine = 1

for line in open('sequence.txt', 'r'):

    if(numLine==1):
        brojeviIzFile = [float(x) for x in line.split(" ")[0:-1]]

    elif(numLine==2):   
        sumaFloat = float(line)
    numLine += 1

print('Broj iz druge linije(%.1f) %s isti kao zbroj brojeva iz prve(%.1f)'\
     % (sum(brojeviIzFile), 'nije' if sum(brojeviIzFile)!=sumaFloat else 'je',\
     sumaFloat))

    
