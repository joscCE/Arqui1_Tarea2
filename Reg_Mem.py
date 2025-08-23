class Reg_mem:
    def __init__(self):
        self.cont = {}   
    
    def Write(self, address, value):
        self.cont[address] = value   
    
    def Read(self, address):
        return self.cont.get(address, None)  
    
