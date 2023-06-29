import csv

contador=0
with open('202004_AuxilioEmergencial_PEQUENO.csv','r',encoding='ISO-8859-1') as infile:
    leitura=csv.reader(infile,delimiter=',')
    cabec=next(leitura)
    #print(cabec[1])
    print(cabec)
    for linha in leitura:
        #uf=linha[0]
        #nome=linha[1]
        #nis=linha[2]
        #valor=linha[3]	       
        contador=contador+1
print(linha)