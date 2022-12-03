#plan: 
# 1.lese fra fil 
# 2. for hver linje:
# 3. Sjekke om seier eller ikke. 
#    om seier vant med hva
# 4.  telle poeng

#ABC=Stein papir saks
#XYZ=Stein papir saks
#så: X slår C, Y slår A og Z slår B.  
# lager en liste med seiere:
seiere=["A Y", "B Z", "C X"]
uavgjort=["A X", "B Y", "C Z"]
# dicts med tilsvarende poeng for formen vi velger: 
valgtBonus={
    "X":1,
    "Y":2,
    "Z":3
}
#dict for poeng for spillet
spillPoeng={
    "tap":0,
    "uavgjort":3,
    "seier":6
}

fil=open("dag2\input.txt")

poeng=0
for linje in fil:
    score=0
    linje=linje[0:3]
    if linje in seiere:
        score+=spillPoeng["seier"]
    elif linje in uavgjort:
        score+=spillPoeng["uavgjort"]
    #om tap: ingen spill poeng
    
    score+=valgtBonus[linje[2]] #legger til poeng fra valgt type
    #print(score)
    poeng+=score
print(poeng)

