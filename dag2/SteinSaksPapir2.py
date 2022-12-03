#plan: 
# 1.lese fra fil 


#ABC=Stein papir saks
## Del to, nå betyr XYZ andre ting. 
#X -> tap, Y-> uavgjort, Z-> vinn.

# dicts med tilsvarende poeng for formen vi må velge: 

#dict for poeng for spillet
spillPoeng={
    "X":0,
    "Y":3,
    "Z":6
}
 
valgtBonus={
    "A":1, #vi velger Stein, 1p
    "B":2, #vi velger papir, 2p
    "C":3 # vi velger saks, 3p
}
fil=open("dag2\input.txt")
valg="ABC"


poeng=0
for linje in fil:

    score=0
    score+=spillPoeng[linje[2]]

#om tap, velger en bak.
#om uavgjort velger samme.
#om seier velger en frem.
    pos=valg.index(linje[0]) #0 1 2
    pos+= int((score - 3)/3)     #om vi taper, fjerner 1, om uavgjort legger til 0, om seier legger til 1
    pos%=3  #mod operator, -1 blir til 2, 3 til 0.

    score+=valgtBonus[valg[pos]]
   
    poeng+=score
    #print(score)
print(poeng)

