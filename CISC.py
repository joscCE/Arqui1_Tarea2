from Mem import Mem
from Alu import Alu
from PC import PC

class CISC:
    def __init__(self, Instr):
        self.Memory = Mem()              
        self.Alu_unit = Alu()
        self.pc  = PC(Instr)  
        self.Addres = []
        self.A =0
        self.B = 0
        self.ciclos = 0 
        self.Use_Instr = 0


    def Exec(self):

        self.op, self.args = self.pc.Fetch().split(" ", 1)
        self.Addres = [x.strip() for x in self.args.split(",")]
        print(self.Addres)
        if(self.op == "SUMMEM"):
            self.SUMMEN()

        elif(self.op == "CMP"):
            self.CPM()
        else:
            print("ERROR: Deje de inventar instrucciones use SUMMEM!")
        

    def SUMMEN(self):
        self.A = self.Memory.Read(self.Addres[1])
        print("A: ", self.A)
        self.B = self.Memory.Read(self.Addres[2])
        print("B: ", self.B)  
        result = self.Alu_unit.Sum(self.A, self.B)      
        print(result)
        self.Memory.Write(self.Addres[0], result)

    def CPM(self):
        self.A = self.Memory.Read(self.Addres[0])
        print("A: ", self.A)
        self.B = self.Memory.Read(self.Addres[1])
        print("B: ", self.B) 
        self.Memory.Write("CPM", self.A == self.B)

