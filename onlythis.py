import os, sys
from Bio import SeqIO

arq_entrada=sys.argv[1]
tipo=sys.argv[2]

for line in SeqIO.parse(arq_entrada, "fasta"):
    if tipo in line.description:
        print ">",line.description,"\n",line.seq

