from Mem import Mem
from Alu import Alu

class CISC:
    def __init__(self):
        self.Memory = Mem()              
        self.Alu_unit = Alu()  
        self.Addres = []
        self.A =0
        self.B = 0

    def Exec(self, Instr):
        self.op, self.args = Instr.split(" ", 1)
        self.Addres = [x.strip() for x in self.args.split(",")]

        self.SUMMEN()

    def SUMMEN(self):
        self.A = self.Memory.Read(self.Addres[1])
        print("A: ", self.A)
        self.B = self.Memory.Read(self.Addres[2])
        print("B: ", self.B)  
        result = self.Alu_unit.Sum(self.A, self.B)      
        print(result)
        self.Memory.Write(self.Addres[0], result)
