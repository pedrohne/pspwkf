import os, sys
from Bio.Seq import Seq

genoma=Seq("AGTACACTGGT")

print genoma.complement()#imprime a fita complementar
