import os, sys
from Bio import SeqIO

arq_entrada=sys.argv[1]

patch=os.getcwd()
os.mkdir("yourproteins")
sys.path.append("../Python27/Bio")

for line in SeqIO.parse(arq_entrada, "fasta"):
    os.chdir("yourproteins")
    temp=open(line.description,"w")
    SeqIO.write(line,temp,"fasta")
    os.chdir(patch)
temp.close()    
    
