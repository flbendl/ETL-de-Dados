import csv

contador=0
with open('202005_AuxilioEmergencial_NOVISSIMO.csv','r',encoding='ISO-8859-1') as infile:
    leitura=csv.reader(infile,delimiter=';')
    cabec=next(leitura)
    #print(cabec[1])
    print(cabec)
    for linha in leitura:
        if contador == 3000:            		
            break
        else:
            print(linha)		
            contador=contador+1
#uf=linha[0]
#nome=linha[1]
#nis=linha[2]
#valor=linha[3]
#print(uf,nome,nis,valor)
#print()
#print(linha)