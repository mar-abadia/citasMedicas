class Medico:
    def __init__(self, id_medico, nombre, especialidad):
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Médico {self.id_medico}: {self.nombre}, Especialidad: {self.especialidad}"