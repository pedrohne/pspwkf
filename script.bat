@echo off
cls
set /p sequence=Nome do arquivo GB: 
set /p feature=Nome da feature:
start python exclude_hypothetical.py %sequence% %feature% > sequencenohyp.gb
start python gbtofaa sequencenohyp.gb > sequencenohyp.fasta

echo As proteínas hipotéticas foram retiradas e o arquivo %sequence% foi convertido para sequencenohyp.gb com sucesso!