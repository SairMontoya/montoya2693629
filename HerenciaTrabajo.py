class Empleado:
    counter = 0  # Variable de clase para contar la cantidad de objetos creados

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        Empleado.counter += 1

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def calcular_salario_hora(self):
        horas_trabajo_diarias = 8
        dias_trabajo_semana = 5
        salario_hora = self.salario / (horas_trabajo_diarias * dias_trabajo_semana)
        return salario_hora



Empleado1 = Empleado("Andres Montoya", "Analista", 2000)

print(f"Salario por hora de {Empleado1.get_nombre()}: ${Empleado1.calcular_salario_hora():.2f}")