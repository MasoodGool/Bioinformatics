def align(AA1,AA2):
    x=0
    star=""
    top=0
    bot=0
    for x in range(len(AA1)):        
        if AA1[x] == AA2[x]:
            top=top+1
            star=star+"*"
        else:star= star+"_"
    ans= str(top/float(len(AA1))*100)
    print "AA Sequence 1: "+AA1
    print "AA Sequence 2: "+AA2
    print '\t'+"       "+star
    print "Alignment: "+ans[0:3]+"%"

m = open('mutatedDNA.txt','r')
n = open('normalDNA.txt','r')
for line in n:
    AA1=line
    print AA1
print "===="
for line in m:
    AA2=line    
    print AA2
align(AA1,AA2)
m.close()
n.close()

