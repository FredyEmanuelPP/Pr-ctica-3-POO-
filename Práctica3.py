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
