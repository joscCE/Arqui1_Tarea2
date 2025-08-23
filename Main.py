
from CLK import CLK
from PC import PC
import time

intrucciones = [
"SUMME",
"ADDA",
"HOLI"
]


pc  = PC(Instrucciones = intrucciones)


for n in range(len(intrucciones)):
    print(pc.Fetch())
    time.sleep(0.5)


 
