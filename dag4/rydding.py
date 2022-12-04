
#plan
"""
1. lese fra fil
2. finne start stop for begge alver
3. sammenligne om start og stop er innenfor den andre alven.
4. summere opp antall som er inneholt i den andre alvens opgaver.
"""

fil = open("dag4\input.txt")
def inneholt(a_start,a_slutt,b_start,b_slutt)->bool:
    """ sjekker om start og slutt på a ligger innenfor start og slutt på b"""
    if a_start>=b_start and a_slutt<=b_slutt:
        return True
    return False

overlappendePar=0
ingenOverlapp=0
antall=0
for linje in fil:
    linje=linje.replace("\n","")
    # prøvde en enlinjer, men det ble med en tolinjer. Denne deler opp linjen i to over "," som a,b og så i to en gang til over "-"
    a,b=[j.split("-") for j in linje.split(",")]
    a,b=[ int(i) for i in a],[int(j) for j in b] #gjør om a,b til heltall.

    
    #a[0],a[1],b[0],b[1] vil være start og slutt punktene.

    
    if inneholt(a[0],a[1],b[0],b[1]):
        overlappendePar+=1
    
    elif inneholt(b[0],b[1],a[0],a[1]):
        overlappendePar+=1
     

    # løser del to
    #plan? Sjekker først om noe av a ligger inne i b, om det gjør det så har vi overlapp. 
    # om ikke overlapp så sjekker vi om b ligger inne i a.  Her bruker jeg lister, da jeg er lei a_start etc...
    overlapp=False
    
    for i in a:
        if i>=b[0] and i<=b[1]:
            # en av a ligger inne i b mellomrommet:
            overlapp=True
    if not overlapp:
        for i in b:
            if i>=a[0] and i<=a[1]:
                # en av b ligger inne i a:
                overlapp=True
    if overlapp:
        antall+=1
   
print("antall noe overlapp",antall)
print("full overlapp",overlappendePar)
    