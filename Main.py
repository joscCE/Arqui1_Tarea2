
from CLK import CLK
from PC import PC
import time
from CISC import CISC
from RISC import RISC


print("CISC --------------------------------------------------------------------------------------------------")

#programa CISC

instrucciones_cisc = [
    "SUMMEM 21, 1, 11",
    "SUMMEM 22, 2, 12",
    "SUMMEM 23, 3, 13",
    "SUMMEM 24, 4, 14",
    "SUMMEM 25, 5, 15",
    "SUMMEM 26, 6, 16",
    "SUMMEM 27, 7, 17",
    "SUMMEM 28, 8, 18",
    "SUMMEM 29, 9, 19",
    "SUMMEM 30, 10, 20",
    "CAMPO, 1, 2, 3"   #verifica que la instruccion existe
]

#instancia CISC

Cisc = CISC(Instr=instrucciones_cisc)

#cargar en memoria los dos vectores:
for i in range(1, 11):
    Cisc.Memory.Write(str(i), i)          # vector 1
    Cisc.Memory.Write(str(i+10), i*2)     # vector 2 


for n in range(len(instrucciones_cisc)):
    Cisc.Exec()
    time.sleep(0.6) #esto es para separar cada instruccion, = 3 ciclos

#resultado

print("Vector resultante (21-30):")
for i in range(21, 31):
    print(f"Mem[{i}] = {Cisc.Memory.Read(str(i))}")
print("Cantidad de ciclos: ", Cisc.ciclos)
print("Cantidad de Instrucciones: ", Cisc.Use_Instr)


print("RISC --------------------------------------------------------------------------------------------------")




# programa RISC equivalente
instrucciones_risc = [
    "TRAER R1, 1",
    "TRAER R2, 11",
    "SUMAR R3, R1, R2",
    "ESCRIBIR 21, R3",

    "TRAER R1, 2",
    "TRAER R2, 12",
    "SUMAR R3, R1, R2",
    "ESCRIBIR 22, R3",

    "TRAER R1, 3",
    "TRAER R2, 13",
    "SUMAR R3, R1, R2",
    "ESCRIBIR 23, R3",

    "TRAER R1, 4",
    "TRAER R2, 14",
    "SUMAR R3, R1, R2",
    "ESCRIBIR 24, R3",

    "TRAER R1, 5",
    "TRAER R2, 15",
    "SUMAR R3, R1, R2",
    "ESCRIBIR 25, R3",

    "TRAER R1, 6",
    "TRAER R2, 16",
    "SUMAR R3, R1, R2",
    "ESCRIBIR 26, R3",

    "TRAER R1, 7",
    "TRAER R2, 17",
    "SUMAR R3, R1, R2",
    "ESCRIBIR 27, R3",

    "TRAER R1, 8",
    "TRAER R2, 18",
    "SUMAR R3, R1, R2",
    "ESCRIBIR 28, R3",

    "TRAER R1, 9",
    "TRAER R2, 19",
    "SUMAR R3, R1, R2",
    "ESCRIBIR 29, R3",

    "TRAER R1, 10",
    "TRAER R2, 20",
    "SUMAR R3, R1, R2",
    "ESCRIBIR 30, R3",
]

# instancia RISC
Risc = RISC(Instr=instrucciones_risc)

# cargar en memoria los dos vectores:
for i in range(1, 11):
    Risc.Memory.Write(str(i), i)          # vector 1
    Risc.Memory.Write(str(i+10), i*2)     # vector 2 

for n in range(len(instrucciones_risc)):
    Risc.Exec()
    time.sleep(0.2) # = 1 ciclo

# resultado
print("Vector resultante (21-30):")
for i in range(21, 31):
    print(f"Mem[{i}] = {Risc.Memory.Read(str(i))}")
print("Cantidad de ciclos: ", Risc.ciclos)
print("Cantidad de Instrucciones: ", Risc.Use_Instr)
