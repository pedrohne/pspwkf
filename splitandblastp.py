import os, sys
from Bio import SeqIO
from Bio.Blast import NCBIWWW

arq_entrada=sys.argv[1]

for line in SeqIO.parse(arq_entrada, "fasta"):
    #proteina=">"+line.description+"\n"+line.seq
    temp=open(line.description,"w")
    SeqIO.write(line,temp,"fasta")
    
temp.close()

for line in SeqIO.parse(arq_entrada, "fasta"):
    arquivo = SeqIO.read(line.description, format="fasta")
    print "Iniciando busca no NCBIWWW..."
    resultado = NCBIWWW.qblast("blastp", "pdb", arquivo.seq, format_type="Text")
    print resultado.read()
    print "Busca concluida."

    
