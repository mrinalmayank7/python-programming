Write1=open('TEXTFILE3.txt','a')
Write1.write("I like to have Pizza with friends \n") 
Write1.write("I used to invlove in creative work in free time\n") 
Write1.close()

READFILE = open("TEXTFILE3.txt", "r")
dry = dict()

for i in READFILE :
    i= i.strip()
    i= i.lower()
    STRING = i.split(" ")

    for j in STRING :
        if j in dry:
            dry[j] = dry[j] + 1
        else: 
            dry[j] = 1

import sys
for keys in list(dry.keys()):
    W2=open('WORDS.txt', 'a')
    sys.stdout = W2 
    print(keys , ":", dry[keys])
W2.close()


    

