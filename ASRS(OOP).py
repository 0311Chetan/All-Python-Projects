class Employees:
    def __init__(self,nEmpID,sName):
       super().__init__()
       self.__nEmpID=999
       self.__sName='No Name'
    
       self.nID=nEmpID
       self.sNam=sName
    def printDetails(self):
        print("Employees::printDetails with ID   ",self.nID)
        print( "Employees::printDetails with Name ",self.sNam)
   
    
    def __del__(self):
        print("Employees::~Employees() with ID ",self.nID)
        
        
p1=Employees(99878,'joe')
p1.printDetails()
del p1
print('============================================')
class Hardware:
    def __init__(self):
        print("Hardware::Hardware() ...")
        
    def  printDetails(self):
        print( "Hardware::printDetails ...")
        
    def __del__(self):
        print("Hardware::~Hardware() ...")
        
p2=Hardware()
p2.printDetails()
del p2            
print('============================================')


class Location:
    def __init__(self,xLocation,yLocation):
        self.__xLocation=0
        self.__yLocation=0
        
        self.xx=xLocation
        self.yy=yLocation
        
    def printDetails(self):
        print("Location::printDetails with xLocation " ,self.xx)
        print("Location::printDetails with yLocation " ,self.yy)
        
    def __del__(self):
        print("Location::~Location() with xLoc ",self.xx)
        
p3=Location(10,15)
p3.printDetails()
del p3

print('============================================')

class Operations:
    def __init__(self):
        self.nOpnCountStore=0
        self.nOpnCountRetrieve=0
        
    def printDetails(self):
        print("Operations::printDetails Number of storing Operations carriedout    = ",self.nOpnCountStore)
        print("Operations::printDetails Number of retrieving Operations carriedout =  ",self.nOpnCountRetrieve)
        
    #def StoreOperations(self,op,prd,hw,loc):
        
   # def RetrieveOperations(self,op,prd,hw,loc):
        
        
    def __del__(self):
        print("Operations::~Operations() .... ")
        
p5=Operations()
p5.printDetails()
del p5

print('============================================') 

class Opertaor(Employees):
    
    def __init__(self,nID,sNam,nMachID):
       
        self.__nMachID=9999
        self.MachID=nMachID
        print("Operator::Operator(Param) with Machine ID ", self.MachID)
        
    def __del__(self):
        print("Operator::~Operator() with Machine ID " )
    
    def printDetails(self):
        print("Operator::printDetails with Machine ID " ,self.MachID)
        
p4=Opertaor(984,'Helo',489)
p4.printDetails()
del p4
    

print('============================================')      
        
        
class Product:
    def __init__(self,nProdID,sProdDesc):
        self.__nProdID=999
        self.__sProdDesc='NoProdname'
        self.Id = nProdID
        self.descri=sProdDesc
        
    def printDetails(self):
        print("Product::printDetails with ID ",self.Id)
        print("Product::printDetails with Description ",self.descri)
        
    def __del__(self):
        print("Product::~Product() with ID " ,self.Id)
        
p7=Product(97,'Oreo')
p7.printDetails()
del p7
print('============================================')
class Rack:
    
    
    def __init__(self,nWidth,nHeight, nDepth,currentLocation):
        self.__nWidth=0
        self.__nHeight=0
        self.__nDepth=0
        self.__currentLocation=0
        self.width=nWidth
        self.height=nHeight
        self.depth=nDepth
    
    def  AddStorageLocation(Location):
        super().__init__()
        #self.Location=++currentLocation
        #print("Rack::AddStorageLocation ... current location size is ",self.Location)
        
    def __del__(self):
        print("Rack::~Rack()  ...")
        
    def printDetails(self):
        print("Rack::printDetails with width  " ,self.width)
        print("Rack::printDetails with height " ,self.height)
        print( "Rack::printDetails with depth  " ,self.depth)
        
p6=Rack(44,55,77,0)

p6.printDetails()
del p6
print('============================================') 

class warehouse:
    def __init__(self,nID,sName):
        self.__nID=999
        self.__sName='NoName'
        
        self.Id=nID
        self.Name=sName
       
        
    def __del__(self):
        print("Warehouse::~Warehouse() with ID ",self.Id)
        
    def printDetails(self):
        print("Warehouse::printDetails with ID   ",self.Id)
        print( "Warehouse::printDetails with Name ", self.Name)

        
p9=warehouse(487,'Amazon')
p9.printDetails()


        
        
        
        
        
        
        
        
        
        
        