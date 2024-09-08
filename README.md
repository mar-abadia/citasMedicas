Sistema de Gestión de Citas Médicas

Este proyecto es un sistema de gestión de citas médicas que permite a los pacientes agendar, cancelar y gestionar sus citas con los médicos. También permite a los médicos administrar sus horarios de atención, y ofrece reportes y notificaciones automáticas.

#Requisitos

Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

- **Python 3.12**: Asegúrate de que Python esté instalado y configurado correctamente.
- **Flask 2.1.1**: Framework web utilizado para desarrollar la interfaz del sistema.
- **Requests >= 2.25.1**: Librería utilizada para realizar peticiones HTTP dentro del proyecto.

Puedes instalar las dependencias necesarias utilizando `pip`:

`pip install -r requirements.txt`

Contenido del archivo requirements.txt:
`flask==2.1.1
requests>=2.25.1`

Instalación
Sigue los pasos a continuación para configurar y ejecutar el proyecto en tu entorno local:

Clona el repositorio:
`git clone https://github.com/tu_usuario/sistema-gestion-citas-medicas.git
cd sistema-gestion-citas-medicas`

Crea un entorno virtual (opcional pero recomendado):
`python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate`

Instala las dependencias:
`pip install -r requirements.txt`

Ejecuta la aplicación:
`python app.py`

Funcionalidades
Agendamiento de Citas: Permite a los pacientes agendar citas con los médicos disponibles.
Cancelación de Citas: Los pacientes pueden cancelar sus citas y liberar el horario.
Gestión de Horarios: Los médicos pueden registrar y gestionar sus horarios de atención.
Notificaciones: El sistema envía notificaciones automáticas para confirmaciones, recordatorios y cancelaciones de citas.
Reportes: Genera reportes sobre la demanda de médicos y especialidades, así como análisis de tendencias de citas.

Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error o deseas agregar nuevas funcionalidades, por favor abre un issue o un pull request.


