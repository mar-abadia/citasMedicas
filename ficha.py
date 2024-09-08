class Ficha:
    def __init__(self, id_paciente, nombre, edad, historial_medico):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad
        self.historial_medico = historial_medico

    def __str__(self):
        return f"Ficha de {self.nombre} (ID: {self.id_paciente}), Edad: {self.edad}, Historial: {self.historial_medico}"
