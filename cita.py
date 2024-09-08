class Cita:
    def __init__(self, id_cita, id_paciente, id_medico, fecha_hora):
        self.id_cita = id_cita
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.fecha_hora = fecha_hora

    def __str__(self):
        return f"Cita {self.id_cita}: Paciente {self.id_paciente} con Médico {self.id_medico} a las {self.fecha_hora}"
