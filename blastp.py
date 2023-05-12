import os, sys
from Bio.Blast import NCBIWWW
from Bio import SeqIO

arq_entrada=sys.argv[1]

arquivo = SeqIO.read(arq_entrada, format="fasta")

print "Iniciando busca no NCBIWWW..."

resultado = NCBIWWW.qblast("blastp", "pdb", arquivo.seq, format_type="Text")

print resultado.read()

print "Busca concluida."
