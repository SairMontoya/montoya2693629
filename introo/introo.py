class Empleado:
    counter = 0
    def _init_(self , Nombre:str , Cargo:str ,Salario:int):
        self.__nombre = Nombre
        self.__cargo = Cargo
        self.__salario = Salario
        Empleado.counter += 1

    def getNombre (self , Nombre:str):
        self.__nombre = Nombre
        
    def getCargo (self , Cargo:str):
        self.__cargo = Cargo
    
    def getSalario (self , Salario:int):
        self.__salario = Salario
    
    def setNombre (self):
        return self.__nombre
    
    def setCargo (self):
        return self.__cargo
    
    def setSalario (self):
        return self.__salario

    def Salario_Hora (self):
        hora = self.__salario/(48*4)
        return int(hora)
    
from Empleado import*

persona1 = Empleado ("Harold" , "ADSO" , 120000)

persona1.getNombre ("Steven")
persona1.getCargo ("Multimedia")
persona1.getSalario (1160000)

print(persona1.setNombre)
print(persona1.setCargo)
print(persona1.setSalario)

print(persona1.Salario_Hora())
