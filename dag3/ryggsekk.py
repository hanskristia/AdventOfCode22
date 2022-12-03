
#plan: 
"""
1. lese fra fil
2.  dele opp syggsekken
3. finne felles i beholderene
4. oversette til prioritet fra ascii verdien

"""
fil = open("dag3\input.txt")

sumPrioriteter=0
for linje in fil:
    linje=linje.replace("\n","")

    # deler opp ryggsekken i del1 og del2
    lengde=len(linje)
    del1=linje[:lengde//2]
    del2=linje[lengde//2:]
    
    #print(linje, del1,del2)
    overlapp=""
    #finner overlappende element, finnes bedre måter å gjøre dette på.
    for i in del1:
        if i in del2:
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
