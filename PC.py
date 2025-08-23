class PC:
    def __init__(self, Instrucciones):
        self.Instr = Instrucciones
        self.PC = -1  
        
    def Fetch(self):
        self.PC += 1
        return self.Instr[self.PC]

        

    


        
          
    
