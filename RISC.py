from Mem import Mem
from Alu import Alu
from PC import PC
from Reg_Mem import Reg_mem   

class RISC:
    def __init__(self, Instr):
        self.Memory = Mem()              
        self.Alu_unit = Alu()
        self.pc  = PC(Instr)  
        self.Registros = Reg_mem()   # ahora usamos la clase Reg_mem
        self.ciclos = 0 
        self.Use_Instr = 0


    def Exec(self):
        # Traer la instrucción desde el PC
        self.op, self.args = self.pc.Fetch().split(" ", 1)
        self.args = [x.strip() for x in self.args.split(",")]

        if self.op == "TRAER":
            self.Traer()
        elif self.op == "SUMAR":
            self.Sumar()
        elif self.op == "ESCRIBIR":
            self.Escribir()
        else:
            print("ERROR: Instrucción no válida en RISC")


    def Traer(self):
        # TRAER Rx, dir   (carga en un registro el valor desde memoria)
        reg = self.args[0]
        direccion = self.args[1]
        valor = self.Memory.Read(direccion)
        self.Registros.Write(reg, valor)
        print(f"TRAER {direccion} → {reg} = {valor}")
        self.ciclos += 1
        self.Use_Instr += 1


    def Sumar(self):
        # SUMAR Rdest, Rsrc1, Rsrc2   (suma dos registros y guarda en destino)
        dest, r1, r2 = self.args
        v1 = self.Registros.Read(r1)
        v2 = self.Registros.Read(r2)
        result = self.Alu_unit.Sum(v1, v2)
        self.Registros.Write(dest, result)
        print(f"SUMAR {r1}({v1})+{r2}({v2}) → {dest} = {result}")
        self.ciclos += 1
        self.Use_Instr += 1


    def Escribir(self):
        # ESCRIBIR dir, Rx   (guarda el valor de un registro en memoria)
        direccion, reg = self.args
        valor = self.Registros.Read(reg)
        self.Memory.Write(direccion, valor)
        print(f"ESCRIBIR {reg} ({valor}) → {direccion}")
        self.ciclos += 1
        self.Use_Instr += 1
