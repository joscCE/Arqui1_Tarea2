
from CLK import CLK
from PC import PC
import time
from CISC import CISC




intrucciones = [
"SUMMEM 1, 3, 4",
"CMP 2, 4",
"HOLI 1, 3, 4"
]


Cisc = CISC(Instr=intrucciones)
for n in range(len(intrucciones)):
    Cisc.Exec()
    time.sleep(0.5)


 
