class Reg_mem:
    def __init__(self):
        self.cont = {
    "R1": 0,
    "R2": 0,
    "R3": 0,

        }

    
    def Write(self, address, value):
        self.cont[address] = value   
    
    def Read(self, address):
        return self.cont.get(address, None)  
    
