

""" Jajaj lage eget filsystem?"""
#antageligvis enklere måter å løse dette på, f.eks med et enkelt tre. Men alt 1 høres artigere ut.

class Dir:
    currDir=None
    root=None
    def __init__(self,name, parent):
        self.name=name
        self.parent=parent
        self.space=0
       
        self.ls={}


    
    def changeDir(self, input):
        if input == "..":
            Dir.currDir=self.parent
        elif input == "/":
            Dir.currDir=Dir.root
        else:
            Dir.currDir=self.ls[input]

    def updateSpace(self, space):
        self.space+=space
        if self.parent != None:
            self.parent.updateSpace(space)

    def addToDir(self, split:list):
        # her er det mulig å bruke noe kwargs tror jeg
        if split[0]=="dir":
            ## legger til ny mappe, antar unikt navn
            self.ls[split[1]]=Dir(split[1],self)
            # alternativt legge til currDiv som denne diven. 
            #mappen veier ingenting.
        else :
            ## legger til ny fil i ls
            space=int(split[0])
            self.ls[split[1]]=space
            ## legger også til vekten av filen i alle overordnede mapper:
            self.updateSpace(space)
    def listDirs(self, nest=0):
        spacing="\t"*nest
        print(f"{ spacing} - {self.name} (dir, size={self.space}) ")
        nest+=1
        spacing="\t"*nest
        for navn,fil in self.ls.items():
            if type(fil)==int:
                # en fil
                print(f"{ spacing} - {navn} (file, size={fil}) ")
            else:
                #en dir:
                fil.listDirs(nest)
    
    
    def cullDirs1(self,maks,curSum=0):
        """ Går rekursivt igjennom alle dir's om den veier mer enn maks legges vekten til curSum"""
        #her vektes mapper flere ganger så burde vel være slik: Kunne ha vært del 2?
        """ går rekursivt igjennom treet, ser om grein veier over max.
        om den gjør det kaller vi rekursivt denne nedover på dir's
        om grein veier under max, vill den fjernes og legges til curSum.
        """ 
        print(self.name, self.space, curSum)
        if self.space<=maks:
            curSum+=self.space
        
        for navn,fil in self.ls.items():
            if type(fil)==int:
                ## telles ikke
                pass
            else:
                curSum=fil.cullDirs1(maks,curSum)
        return curSum  

    def cullDirs2(self,cullSize, BestOption=root):
        """ Går rekursivt igjennom alle dir's 
        om den veier mer enn cullSize og mindre enn BestOption, så blir den best option.
        om den veier mer vil den og sjekke alle dirs innenfor.
        om den veier mindre enn cullSize skjer inngenting.
        returnerer bestOption.
        """ 
        #print(self.name, self.space, "valgt: ",BestOption.name,BestOption.space)
        if self.space > cullSize:
            if self.space<BestOption.space:
                BestOption=self
            for navn,fil in self.ls.items():
                if type(fil)==int:
                    ## telles ikke
                    pass
                else:
                    BestOption=fil.cullDirs2(cullSize,BestOption)
            return BestOption  

        else:
            return BestOption
        
        

root=Dir("/",None)
Dir.root=root
Dir.currDir=root

fil=open("dag7/input.txt")

for linje in fil:
    linje=linje.replace("\n","")
    deler=linje.split(" ")
    if deler[0]=="$":
        ## en kommando:
        if deler[1]=="cd":
            Dir.currDir.changeDir(deler[2])
        else:
            # en ls
            pass
    else:
        # ny input som skal legges til nåværende fil:
        # dette håndteres av add to Dir funksjonen.
        Dir.currDir.addToDir(deler)
root.listDirs()
#print(root.cullDirs1(100000))

memory=70000000
availableMemory=memory-root.space
neededMemory=30000000
cullSize=neededMemory-availableMemory

print(root.cullDirs2(cullSize, root).space)