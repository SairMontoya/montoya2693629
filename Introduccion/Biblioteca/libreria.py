class Usuario:
    def __init__(self, nombre, apellido, identificacion):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__identificacion = identificacion


    def  setNombre ( self , nombre):
        self.__nombre=nombre
    def  getNombre( self):
        return self.nombre
    def  setApellido( self , apellido ):
        self.__apellido=apellido
    def getApellido(self):
        return self.apellido
    def setIdentificacion(self , identificacion):
        self.__identificacion=identificacion
    def getIdentificacion(self):
        return self.identificacion
    
    def  verificar(self):
        if self.__nombre =="Andres" and self.__apellido == "Montoya":
           print("La informacion del usuario es correcta")
        else:
           print("la informacion del ususario es inconrrecta")
    def creacionCuenta(self):
        if self.__nombre =="Andres" and self.__identificacion == "1012337983":
            print("la informacion ingresada es correcta")
        else:
            print("la infomacion ingresada es incorrecta")

    def InformacionDelLibro(self):
        while True:
            print("1. informacion del libro/seleccione un libro")
            print("2. Python Crash Course", "Eric Matthes", 2019)
            print("3. Clean Code", "Robert C. Martin", 2008)

            eleccion = input("digite su eleccion")

            if eleccion == "1":
                print("informacion del libro")
             
            elif eleccion == "2":

                print ("El libro seleccionado fue  Python Crash Course ")
                print ("Autor eric matthes")
                print ("Año de publicacion 2019")
            
            elif eleccion == "3":
                print("El libro seleccionado fue clean code")
                print("Autor Robert C")
                print("Año de publicacion 2008")

            else:
                print ( "Opción no válida. Vuelva a intentarlo" )