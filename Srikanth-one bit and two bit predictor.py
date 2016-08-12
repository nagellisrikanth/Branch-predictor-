#Srikanth goud nagelli 
#python 
#canopy simulator 
#One bit and Two bit counter predictor
###################################### 
#reading input trace file 
f=open('trace','r') 
l=f.readlines()
b=[]
i=0
# checking the distance b/w i/p trace and finding the branches 
for i in range (len(l)-1):   
    if (((int(l[i+1],16))-(int(l[i],16))) >15) or (((int(l[i+1],16))-(int(l[i],16))) < 0): 
        b.append(l[i])
        i=i+1
    print l[i]        
print len(b)
print b 
# removing duplicates 
def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output
#Unique branches 
T=uniq(b) 
i=0
for i in range (len(T)):
    print T[i][-6:]
print len(T)
# defining a hash table
p=[]
j=0
for j in range(len(T)):
    x=bin(int(T[j],16))[-5:]
    p.append(x)
print p
print len(p)
M=uniq(p)
print M
print len(M)
p1={}
for i in range(len(M)):
    p1[M[i]]=1
print p1
cp=0
mp=0

for i in range (len(l)-1):
    d=(int(l[i+1],16)-int(l[i],16))
    for j in range (len(T)):
        if( T[j]==l[i]):
            key=bin(int(T[j],16))[-5:]
            if(d >15 or d<0):
                if (p1[key]==1):
                    cp=cp+1
                else:
                    mp=mp+1
                    p1[key]=1
        
            else:
                if (p1[key]==0):
                    cp=cp+1
                else:
                    mp=mp+1
                    p1[key]=0
# accuracy of the predictor 
print "incorrect predictor_1 bit "                   
print mp
print "correct predictor_1 bit "
print cp 
print "correct predictor_1 bit- accuracy "
effi=((cp)/float (mp+cp));
print float(effi)*100   
## Two bit predictor ##
# hashing function 
p2={}

for i in range(len(T)):
    t= bin(int(T[i],16))[-4:]
    p2[t]=1
print p2
print len(p2)
cp2=0
mp2=0

# checking all the states 
for i in range (len(l)-1):
    d=(int(l[i+1],16)-int(l[i],16))
    for j in range (len(T)):
        if( T[j]==l[i]):
            key=bin(int(T[j],16))[-4:]
            if(d >15 or d<0):
                if p2[key]==0:
                     mp2=mp2+1
                     p2[key]=1
                elif p2[key]==3:
                    cp2=cp2+1
                    p2[key]=3
                elif p2[key]==2:
                     cp2=cp2+1
                     p2[key]=3
                elif p2[key]==1:
                     cp2=cp2+1
                     p2[key]=3
            else :        
                if p2[key]==0:
                   cp2=cp2+1
                   p2[key]=0
                elif p2[key]==3:
                   mp2=mp2+1
                   p2[key]=2
                elif p2[key]==2:
                   mp2=mp2+1
                   p2[key]=0
                elif p2[key]==1:
                   cp2=cp2+1
                   p2[key]=0
                   
                   
# accuracy of the two bit predictor                
print p2  
print "incorrect predictor_2 bit "                    
print mp2
print "correct predictor_2 bit "
print cp2
print "correct predictor_2 bit- accuracy " 
effi=((cp2)/float (mp2+cp2));
print float(effi)*100  


    
