
#plan

"""
hente inn inputs. Litt vanskeligere nå
1. Ta in linjer
2. opprete nåværende lister.
3 Så:
Arbeider med kassene som lister med lister i.
bruker disse som en LiFo-kø
funksjon for å flytte en kasse
funksjon for å si antall ganger funk ovenfor kjøres.
"""

fil = open("dag5\input.txt")

oppstart=True
antall=9
container=[]
for i in range(antall):
    container.append([])

while oppstart:
    linje=fil.readline()
    if linje[1]=="1":
        oppstart=False
    else:
        for i in range(0,antall):
            # print(i,linje[i*4+1])
            if linje[i*4+1]!=" ":
                container[i].insert(0,linje[i*4+1])


  
# 1   2   3   4   5   6   7   8   9 
linje=fil.readline() # leser den tomme linjen
for linje in fil:
    linje=linje.replace("\n","")
    # print(linje)
    # print([i for i in container])
    inputs=linje.split(" ")
    antallganger=int(inputs[1])
    fra=int(inputs[3])-1
    til=int(inputs[5])-1
    for i in range(antallganger):
        #antall ganger vi skal flytte
        container[til].append(container[fra].pop())

print(container)
svar=""
for i in container:
    svar+=i[-1]
print(svar)

