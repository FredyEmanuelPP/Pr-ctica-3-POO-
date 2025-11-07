"""
Proyecto de Casa Inteligente 

Este script simula la gestión de dispositivos IoT en una casa inteligente,
utilizando Clases Abstractas (ABC) para definir una interfaz común
y composición para manejar el conjunto de dispositivos.
"""

# Importamos los módulos necesarios para crear Clases Abstractas (ABC)
from abc import ABC, abstractmethod
import time

# --- 1. CLASE ABSTRACTA BASE ---

class Dispositivo(ABC):
    """
    Clase Abstracta Base (ABC) que define la interfaz común para
    todos los dispositivos inteligentes.
    
    Atributos:
        _id_dispositivo (str): Identificador único (protegido).
        _estado (str): Estado actual del dispositivo, ej: "apagado" (protegido).
    """
    
    def __init__(self, id_dispositivo):
        """Inicializa un nuevo dispositivo."""
        # Usamos guión bajo para indicar que son atributos "protegidos"
        # (convención de Python para atributos internos)
        self._id_dispositivo = id_dispositivo
        self._estado = "apagado"
        print(f"Dispositivo {self._id_dispositivo} creado (estado inicial: {self._estado}).")

    # --- Métodos de propiedad (Getters) ---
    # Permiten leer los atributos protegidos de forma segura

    @property
    def id_dispositivo(self):
        """Obtiene el ID del dispositivo."""
        return self._id_dispositivo

    @property
    def estado(self):
        """Obtiene el estado actual del dispositivo."""
        return self._estado

    # --- Métodos Abstractos ---
    # Estos métodos DEBEN ser implementados por cualquier subclase

    @abstractmethod
    def encender(self):
        """Define cómo se enciende el dispositivo."""
        pass

    @abstractmethod
    def apagar(self):
        """Define cómo se apaga el dispositivo."""
        pass

    @abstractmethod
    def mostrar_datos(self):
        """Muestra la información específica y estado del dispositivo."""
        pass

# --- 2. SUBCLASES CONCRETAS ---

class LuzInteligente(Dispositivo):
    """
    Subclase para una Luz Inteligente.
    Hereda de Dispositivo.
    """
    
    def __init__(self, id_dispositivo, intensidad=0):
        # Llamamos al constructor de la clase padre (Dispositivo)
        super().__init__(id_dispositivo)
        self._intensidad = intensidad

    @property
    def intensidad(self):
        """Obtiene la intensidad de la luz."""
        return self._intensidad
    
    @intensidad.setter
    def intensidad(self, valor):
        """Establece la intensidad, validando que esté en rango."""
        if 0 <= valor <= 100:
            self._intensidad = valor
            if self._estado == "encendido":
                 print(f"Luz {self.id_dispositivo}: Intensidad ajustada al {valor}%.")
        else:
            print("Error: La intensidad debe estar entre 0 y 100.")

    def encender(self):
        """Enciende la luz a una intensidad media por defecto."""
        self._estado = "encendido"
        if self._intensidad == 0:
            self._intensidad = 50  # Intensidad por defecto al encender
        print(f"Luz {self.id_dispositivo} encendida (Intensidad: {self._intensidad}%).")

    def apagar(self):
        """Apaga la luz y pone la intensidad a 0."""
        self._estado = "apagado"
        self._intensidad = 0
        print(f"Luz {self.id_dispositivo} apagada.")

    def mostrar_datos(self):
        """Muestra el estado e intensidad de la luz."""
        print(f"[Luz] ID: {self.id_dispositivo} | Estado: {self.estado} | Intensidad: {self.intensidad}%")


class CamaraSeguridad(Dispositivo):
    """
    Subclase para una Cámara de Seguridad.
    Hereda de Dispositivo.
    """
    
    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self._grabando = False

    @property
    def grabando(self):
        """Indica si la cámara está grabando."""
        return self._grabando

    def encender(self):
        """Enciende la cámara (modo 'standby')."""
        self._estado = "standby" # Un estado más específico que "encendido"
        print(f"Cámara {self.id_dispositivo} encendida (en espera).")
    def apagar(self):
        """Apaga la cámara y detiene cualquier grabación."""
        self._estado = "apagado"
        if self._grabando:
            self.detener_grabacion()
        print(f"Cámara {self.id_dispositivo} apagada.")

    def iniciar_grabacion(self):
        """Inicia la grabación si la cámara está encendida."""
        if self._estado == "standby":
            self._grabando = True
            self._estado = "grabando"
            print(f"Cámara {self.id_dispositivo}: ¡GRABANDO!")
        elif self._estado == "apagado":
            print(f"Cámara {self.id_dispositivo}: No se puede grabar, está apagada.")
        else:
             print(f"Cámara {self.id_dispositivo}: Ya estaba grabando.")

    def detener_grabacion(self):
        """Detiene la grabación."""
        if self._grabando:
            self._grabando = False
            self._estado = "standby" # Vuelve a espera
            print(f"Cámara {self.id_dispositivo}: Grabación detenida.")

    def mostrar_datos(self):
        """Muestra el estado y si está grabando."""
        estado_grabacion = "Sí" if self.grabando else "No"
        print(f"[Cámara] ID: {self.id_dispositivo} | Estado: {self.estado} | Grabando: {estado_grabacion}")


class SensorMovimiento(Dispositivo):
    """
    Subclase para un Sensor de Movimiento.
    Hereda de Dispositivo.
    """
    
    def _init_(self, id_dispositivo):
        super()._init_(id_dispositivo)
        self._movimiento_detectado = False

    @property
    def movimiento_detectado(self):
        """Indica si se ha detectado movimiento recientemente."""
        return self._movimiento_detectado

    def encender(self):
        """Activa el sensor."""
        self._estado = "activo"
        self._movimiento_detectado = False # Resetea al activar
        print(f"Sensor {self.id_dispositivo} activado.")
        
    def apagar(self):
        """Desactiva el sensor."""
        self._estado = "inactivo"
        self._movimiento_detectado = False
        print(f"Sensor {self.id_dispositivo} desactivado.")
    
