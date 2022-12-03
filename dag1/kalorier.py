#plan
#hente inn fil
#opprette liste med sum av hver alvs matmengde

#lese linje for linje
    #bestemme om det er ny alv, eller summe opp.
#finne største tall i listen. 



#hente inn fil

input=open("dag1\calories1.txt")
#lage liste
cals=[]
sumCal=0
#gå igjennom linjene i fila:
for line in input:
    
    if line == "\n": #om ny alv
        cals.append(sumCal)
        sumCal=0
        # print("tom linje!")
    else: #om mat:
        sumCal+=int(line)

print(max(cals))  # top 1 alv, løsning opg 1

cals.sort(reverse=True) #sorterer listen fra størst til minst.
top3=cals[0:3] #henter ut top 3
top3Sum=sum( top3) #summerer top 3 alver
print(top3Sum) #skriver ut løsning opg 2