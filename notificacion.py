class Notificacion:
    def enviar_notificacion(self, mensaje: str, id_paciente: int):
        # Lógica para enviar notificaciones (SMS, correo, etc.)
        print(f"Notificación enviada a Paciente ID {id_paciente}: {mensaje}")

    def enviar_notificacion_cancelacion(self, id_paciente: int, id_cita: int):
        mensaje = f"Su cita ID {id_cita} ha sido cancelada."
        self.enviar_notificacion(mensaje, id_paciente)
