from datetime import datetime
from notificacion import Notificacion
from paciente import Paciente
from medico import Medico
from horario import Horario
from cita import Cita
from reporte import ReporteDemanda, ReporteCancelaciones
from datetime import datetime, time, timedelta

# Implementación de la clase Paciente
class Paciente:
    def __init__(self, id_paciente, nombre):
        self.id_paciente = id_paciente
        self.nombre = nombre

    def __str__(self):
        return f"Paciente(ID: {self.id_paciente}, Nombre: {self.nombre})"

# Implementación de la clase Medico
class Medico:
    def __init__(self, id_medico, nombre, especialidad):
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad
        self.horarios = []

    def agregar_horario(self, fecha, hora_inicio, hora_fin):
        self.horarios.append(Horario(fecha, hora_inicio, hora_fin))

    def esta_disponible(self, fecha_hora):
        # Verifica si la fecha_hora cae dentro de alguno de los horarios disponibles del médico
        for horario in self.horarios:
            if horario.fecha.date() == fecha_hora.date() and horario.hora_inicio <= fecha_hora.time() <= horario.hora_fin:
                return True
        return False

    def __str__(self):
        return f"ID: {self.id_medico}, Nombre: {self.nombre}, Especialidad: {self.especialidad}"

    def ver_horarios(self):
        print(f"Horarios para {self.nombre} (ID: {self.id_medico}):")
        for horario in self.horarios:
            print(horario)

class Horario:
    def __init__(self, fecha, hora_inicio, hora_fin):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def __str__(self):
        return f"{self.fecha.strftime('%d/%m/%Y')}: {self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')}"

# Implementación de las clases para citas
class Cita:
    def __init__(self, id_paciente, id_medico, fecha_hora):
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.fecha_hora = fecha_hora

    def __str__(self):
        return f"Cita(ID Paciente: {self.id_paciente}, ID Medico: {self.id_medico}, Fecha y Hora: {self.fecha_hora})"

class CitaGeneral(Cita):
    pass

class CitaEspecialista(Cita):
    pass

# Implementación del patrón Factory para crear citas
class CitaFactory:
    @staticmethod
    def crear_cita(tipo, id_paciente, id_medico, fecha_hora):
        if tipo == "general":
            return CitaGeneral(id_paciente, id_medico, fecha_hora)
        elif tipo == "especialista":
            return CitaEspecialista(id_paciente, id_medico, fecha_hora)
        else:
            raise ValueError("Tipo de cita no válido")

# Implementación del patrón Singleton en SistemaGestionCitas
class SistemaGestionCitas:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SistemaGestionCitas, cls).__new__(cls, *args, **kwargs)
            cls._instance.citas = []
            cls._instance.medicos = []
            cls._instance.pacientes = []
        return cls._instance

    def __init__(self):
        pass

    def menu_principal(self):
        while True:
            print("\nMenú Principal")
            print("1. Agendar Cita")
            print("2. Cancelar Cita")
            print("3. Ver Citas")
            print("4. Ver Pacientes")
            print("5. Ver Horarios de Médicos")
            print("6. Reporte")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agendar_cita()
            elif opcion == "2":
                self.cancelar_cita()
            elif opcion == "3":
                self.ver_citas()
            elif opcion == "4":
                self.ver_pacientes()
            elif opcion == "5":
                self.ver_horarios_medicos()
            elif opcion == "6":
                self.generar_reporte()
            elif opcion == "7":
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")

    def agendar_cita(self):
        tipo_cita = input("Ingrese el tipo de cita (general/especialista): ")
        id_paciente = input("Ingrese el ID del paciente: ")
        id_medico = input("Ingrese el ID del médico: ")
        fecha_hora = input("Ingrese la fecha y hora de la cita (YYYY-MM-DD HH:MM): ")

        # Verificar si la entrada tiene tanto la fecha como la hora
        if len(fecha_hora.strip().split()) != 2:
            print("Por favor, ingrese tanto la fecha como la hora en el formato correcto (YYYY-MM-DD HH:MM).")
            return

        # Verificar existencia de paciente y médico
        paciente = self.buscar_paciente_por_id(id_paciente)
        medico = self.buscar_medico_por_id(id_medico)
        
        if not paciente:
            print("Paciente no encontrado.")
            return
        if not medico:
            print("Médico no encontrado.")
            return

        # Verificar disponibilidad del médico
        fecha_cita = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
        if not medico.esta_disponible(fecha_cita):
            print("El médico no está disponible en esa fecha y hora.")
            return
        
        # Crear la cita usando la Factory
        cita = CitaFactory.crear_cita(tipo_cita, id_paciente, id_medico, fecha_cita)
        
        # Guardar la cita en el sistema
        self.citas.append(cita)
        print("Cita agendada exitosamente.")

        try:
            fecha_cita = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Fecha o hora inválida. Asegúrese de que la fecha y hora estén en el formato correcto (YYYY-MM-DD HH:MM).")
        return          

    def cancelar_cita(self):
        id_paciente = input("Ingrese el ID del paciente cuya cita desea cancelar: ")
        id_medico = input("Ingrese el ID del médico de la cita: ")
        fecha_hora = input("Ingrese la fecha y hora de la cita (YYYY-MM-DD HH:MM): ")

        # Buscar y cancelar la cita
        fecha_cita = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
        for cita in self.citas:
            if (cita.id_paciente == id_paciente and
                cita.id_medico == id_medico and
                cita.fecha_hora == fecha_cita):
                self.citas.remove(cita)
                print("Cita cancelada exitosamente.")
                return
        
        print("No se encontró ninguna cita con los datos proporcionados.")

    def ver_citas(self):
        if not self.citas:
            print("No hay citas agendadas.")
        else:
            for cita in self.citas:
                print(cita)

    def ver_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados.")
        else:
            for paciente in self.pacientes:
                print(paciente)

    def ver_horarios_medicos(self):
        if not self.medicos:
            print("No hay médicos registrados.")
        else:
            for medico in self.medicos:
                medico.ver_horarios()

    def buscar_medico_por_id(self, id_medico):
        for medico in self.medicos:
            if medico.id_medico == id_medico:
                return medico
        return None

    def buscar_paciente_por_id(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id_paciente == id_paciente:
                return paciente
        return None
    
    def generar_reporte(self):
        print("Seleccione el tipo de reporte:")
        print("1. Reporte demanda")
        print("2. Reporte cancelaciones")
        tipo_reporte = input("Seleccione una opción: ")

        if tipo_reporte == "1":
            self.strategy = ReporteDemanda()
        elif tipo_reporte == "2":
            self.strategy = ReporteCancelaciones()
        else:
            print("Tipo de reporte no válido.")
            return

        fecha_hora = datetime.now()
        self.strategy.generar()
        print(f"Reporte de citas generado el {fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}")

# Ejecución del sistema
if __name__ == "__main__":
    sistema = SistemaGestionCitas()

    # Crear y agregar médicos y pacientes de ejemplo
    medico1 = Medico("001", "Dr. Juan Pérez", "General")
    medico1.agregar_horario(datetime(2024, 9, 11), time(9, 0), time(13, 0))
    medico1.agregar_horario(datetime(2024, 9, 12), time(10, 0), time(14, 0))
    sistema.medicos.append(medico1)

    medico2 = Medico("002", "Dr. Ana Gómez", "Especialista")
    medico2.agregar_horario(datetime(2024, 9, 13), time(15, 0), time(18, 0))
    medico2.agregar_horario(datetime(2024, 9, 14), time(9, 0), time(12, 0))
    sistema.medicos.append(medico2)

    paciente1 = Paciente("001", "Juan Pérez")
    paciente2 = Paciente("002", "María López")
    sistema.pacientes.append(paciente1)
    sistema.pacientes.append(paciente2)

    sistema.menu_principal()