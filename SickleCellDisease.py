def translate(DNA):
    output=""
    while len(DNA)/3 != 0 :
        if DNA[0:3] == ("ATT" or "ATC" or "ATA") :
            output= output +"I"
        elif DNA[0:3] == ("CTT" or "CTC" or "CTA" or "CTG" or "TTA" or "TTG"):
            output= output +"L"
        elif DNA[0:3] == ("GTT" or "GTC" or "GTA" or "GTG"):
            output= output +"V"
        elif DNA[0:3] == ("TTT" or "TTC"):
            output= output +"F"
        elif DNA[0:3] == "ATG" :
            output= output +"M"
        else: output= output +"X"    
        DNA = DNA[3:]
    print output

def txtTranslate(n,m):
    for line in n:
        translate(line)
    print "======="    
    for line in m:
        translate(line)        

def mutate(f):
    normal = open('normalDNA.txt','w')
    mutated = open('mutatedDNA.txt','w')
    f = open('DNA.txt','r+')
    for line in f:
        newA=''
        newT=''
        x=0
        for x in range(len(line)):        
            if line[x] == "a":
                x=x+1
                newA= newA + "A"
                newT= newT + "T"
            else:
                newA = newA + line[x]
                newT = newT + line[x]
        normal.write(newA)
        mutated.write(newT)

    f.close()
    normal.close()
    mutated.close()

f = file('DNA.txt','r+')
mutate(f)
normal = file('normalDNA.txt','r+')
mutated = file('mutatedDNA.txt','r+')
txtTranslate(normal,mutated)

