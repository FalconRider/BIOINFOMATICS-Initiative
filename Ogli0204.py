#   PEPTIDE Simulator  P. Gitschner    2021

# Version 1   an execise
#  Generate a random peptide chain of random length

import random

print('  ')
print("         Oligopeptide Simulator     Just some coding practice ")
print('          P. Gitschner    2021     ')
print("")
print("Oligopeptides are short chains of amino acids (2 to 20) designated by 20 Alpha characters, no J,O,U,X or B,Z here")


print("")
print("Here's 10 random  examples of them")
print("")
for PEP in range(1,11):
    
    LENGTH = random.randint(1,19)
    print(PEP, " Length =    ", LENGTH)
    CHAIN = []

    for CTR in range( 1 , LENGTH +1):
        AA = (random.randint(65,89))     
                 
        if AA == 74: # J        
            AA= 71   # G      
         
        if AA == 79: # O        
            AA= 76   # L       
         
        if AA == 85: # U     
           AA= 83    # S
              
        if AA == 88: # X      
           AA= 86    # V    
        
        if AA == 66: # B    
           AA= 76    # L
          

        # Z eliminated by range selection- no 90
        # substitutions chosen by checking a freq dist     
       
        CHAIN.append(chr(AA)) 


    print("  ",CHAIN)
    print(" ")
        




