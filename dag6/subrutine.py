
fil=open("dag6\input.txt")

line=fil.readline()

l=[]
for i in line:
    l.append(i)
""" plan: Bruker lister, 
Itererer igjennom input ved å: 
legger til og fjerner et element om gangen
for så å sjekke om alle element i listen er unike
"""
# del 1: 4
# del 2: 14
test=[l.pop(0) for i in range(14)]
rec=len(test)
#oppstarten er den vanskelige delen her...

def sjekkUnik(test):
    for i in test:
        if test.count(i)>1:
            return False
    return True
unik=sjekkUnik(test)
while not unik and len(l)>0:
    test.pop(0)
    test.append(l.pop(0))
    rec+=1
    unik=sjekkUnik(test)
print(test,rec)