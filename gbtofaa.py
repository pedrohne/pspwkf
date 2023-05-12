import os, sys

arq_entrada=sys.argv[1]

with open(arq_entrada) as f:
    for line in f:
        line=line.replace(" ['","")
        line=line.replace("']","")
        line=line.replace("['","")
        line=line.replace("\n","")
        print (line)
        
