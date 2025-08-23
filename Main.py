
from CLK import CLK
from PC import PC
import time
from CISC import CISC


Cisc = CISC()

intrucciones = [
"SUMME 1, 3, 4",
"ADDA 1, 3, 4",
"HOLI 1, 3, 4"
]

pc  = PC(Instrucciones = intrucciones)

for n in range(len(intrucciones)):
    Cisc.Exec(pc.Fetch())
    time.sleep(0.5)


 
