class Observer:
    def update(self, message):
        raise NotImplementedError()

class Horario:
    def __init__(self, id_horario, id_medico, fecha, hora_inicio, hora_fin, disponible):
        self.id_horario = id_horario
        self.id_medico = id_medico
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.disponible = disponible
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def __str__(self):
        return f"Horario {self.id_horario}: Médico {self.id_medico} el {self.fecha} de {self.hora_inicio} a {self.hora_fin}, Disponible: {self.disponible}"