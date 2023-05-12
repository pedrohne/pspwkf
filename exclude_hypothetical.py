import os, sys
from Bio import SeqIO

arq_entrada=sys.argv[1]
option=sys.argv[2]

conteudo = SeqIO.read(arq_entrada, "genbank")

for line in conteudo.features:
	if line.type == 'CDS':
            if "hypothetical protein" not in line.qualifiers['product']:
                        if option=="product" or option=="translation":
                                  print ">",line.qualifiers['product']
                                  print line.qualifiers['translation']
                                  
                        elif option=="protein_id":
                            print line.qualifiers['protein_id']
                        else:
                            print "sintax error"
                            print "please use: python program.py sequence_file feature_name"
