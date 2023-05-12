import os, sys
from Bio import SeqIO

arq_entrada=sys.argv[1]
arq_saida=sys.argv[2]

#conteudo = SeqIO.read(arq_entrada, "genbank")
conteudo=open(arq_entrada,"r")
saida=open(arq_saida,"w")

for line in SeqIO.parse(conteudo,"fasta"):
    if((len(line.seq)<150)):
       SeqIO.write(line,saida,"fasta")

saida.close()
