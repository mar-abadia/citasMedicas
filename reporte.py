# reporte.py

from abc import ABC, abstractmethod

# Clase base que define la interfaz para los reportes.
class Reporte(ABC):
    
    @abstractmethod
    def generar(self):
        pass

# Estrategia concreta para generar el reporte de demanda.
class ReporteDemanda(Reporte):
    
    def generar(self):
        print("Generando reporte de demanda...")
        # Aquí iría la lógica para generar el reporte de demanda.

# Estrategia concreta para generar el reporte de cancelaciones.
class ReporteCancelaciones(Reporte):
    
    def generar(self):
        print("Generando reporte de cancelaciones...")
        # Aquí iría la lógica para generar el reporte de cancelaciones.
