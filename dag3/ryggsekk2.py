
#plan: 
"""
1. lese fra fil
2. sammenligne tre og tre linjer.
3. finne felles i de tre beholderene
4. oversette til prioritet fra ascii verdien

"""
fil = open("dag3\input.txt")

sumPrioriteter=0
linjer=fil.readlines()

for i in range(0,len(linjer),3):
    #sjekker tre og tre, fjerner \n
    sekker=[]
    for linje in linjer[i:i+3]:
        sekker.append( linje.replace("\n",""))
    
    
    overlapp=""
    #finner overlappende element, finnes bedre måter å gjøre dette på. Men vi vet at det må være i den første sekken og i de to andre. 
    for i in sekker[0]:
        if i in sekker[1] and i in sekker[2]:
            overlapp=i
    
    # gir prioritet
    prioritet=ord(overlapp)
    if prioritet>96: #om liten bokstav
        prioritet-= 96
    else:
        prioritet-=64
        prioritet+=26
    sumPrioriteter+=prioritet
    #print(overlapp, prioritet)
    
print(sumPrioriteter)
