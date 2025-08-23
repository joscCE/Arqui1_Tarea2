class Mem:
    def __init__(self):
        self.cont = {
    "1": 0,
    "2": 0,
    "3": 2,
    "4": 2,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0
}   
    
    def Write(self, address, value):
        self.cont[address] = value   
    
    def Read(self, address):
        return self.cont.get(address, None)  
    

    
