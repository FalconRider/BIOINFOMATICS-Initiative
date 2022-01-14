#   RNA Simulator  P. Gitschner    2021

import random
print('  ')
print("         RNA Simulator     Just some coding practice ")
print('          P. Gitschner    2021     ')
print("")

#  a list
N=["U","A","C","G"]
CHAIN = []
OPCHAIN = []
CODONS = []
"""
#  a dict
NP={"U":"A","A":"U","C":"G","G":"C"}

print("Nucleotides",N)
print('  ')
print('Pairs   ')
print("given U   get ",NP["U"]  )
print("given A   get ",NP["A"]  )
print("given C   get ",NP["G"]  )
print("given G   get ",NP["C"]  )
print('  ')

"""

START = "TTT"
OPSTART = "AAA"
print('start',START)
STOP = "TGA"
OPSTOP ="ACT"
print('stop ',STOP)
print("")





#length =  6
print(" Input how many nucleotides, length of chain")
length = int(input())


position = 1

print("length", length)

########################### 53
print('  ')
CHAIN.append(START[0])
CHAIN.append(START[1])
CHAIN.append(START[2])

for size in range(length):
    acid = random.randint(1,4)
    if acid == 1:
        AA = "U"
    if acid == 2 :
        AA = "A"
    if acid  == 3:
        AA = "C"
    if acid  == 4:
        AA = "G"  
   
    position = position + 1
    
    CHAIN.append(AA)    
  
#CHAIN.append(STOP)
CHAIN.append(STOP[0])
CHAIN.append(STOP[1])
CHAIN.append(STOP[2])


#Hold = input("hit return to proceed")



print(" RNA  single sided chain   starting with  - - ",START)
print(" RNA  single sided chain   ending with    - - ",STOP)

#print ("If over 200 nucs, printed to file ")

print (" chain  printed to file named  - chainFile.txt    -")

fileName = "rndData.txt"
with open(fileName,'w') as file_object:
    file_object.write(str(CHAIN))

print('  ')

    
    
    











