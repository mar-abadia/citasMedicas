class Observer:
    def update(self, message):
        raise NotImplementedError()

class Paciente(Observer):
    def __init__(self, id_paciente, nombre):
        self.id_paciente = id_paciente
        self.nombre = nombre

    def update(self, message):
        print(f"Paciente {self.id_paciente} recibió el mensaje: {message}")

    def __str__(self):
        return f"Paciente {self.id_paciente}: {self.nombre}"
