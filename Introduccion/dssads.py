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

    def calcular_salario_horas_extras(self, horas_extras):
        horas_diarias_maximas = 2
        salario_hora_extra = self.calcular_salario_hora() * 1.5
        salario_extras = 0

        if horas_extras <= horas_diarias_maximas:
            salario_extras = salario_hora_extra * horas_extras
        else:
            salario_extras = salario_hora_extra * horas_diarias_maximas

        return salario_extras

# Ejemplo de uso de la clase Empleado
empleado1 = Empleado("Andres Montoya", "Analista", 2000)

print(f"{Empleado.counter}")
print(f"{empleado1.get_nombre()}: ${empleado1.calcular_salario_hora():.2f}")
print(f"{empleado1.get_nombre()}: ${empleado1.calcular_salario_horas_extras(3):.2f}")

