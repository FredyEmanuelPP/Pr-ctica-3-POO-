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
    
    
    def simular_movimiento(self):
        """Simula la detección de movimiento."""
        if self._estado == "activo":
            self._movimiento_detectado = True
            print(f"Sensor {self.id_dispositivo}: ¡¡MOVIMIENTO DETECTADO!!")
        else:
            print(f"Sensor {self.id_dispositivo}: Está inactivo, no puede detectar.")

    def mostrar_datos(self):
        """Muestra el estado del sensor y si hay detección."""
        deteccion = "Sí" if self.movimiento_detectado else "No"
        print(f"[Sensor] ID: {self.id_dispositivo} | Estado: {self.estado} | Movimiento Detectado: {deteccion}")


# --- 3. CLASE DE COMPOSICIÓN ---

class CasaInteligente:
    """
    Clase que gestiona todos los dispositivos de la casa.
    Utiliza composición (tiene una lista de objetos Dispositivo).
    """
    
    def _init_(self, nombre):
        self.nombre = nombre
        self._dispositivos = []  # Lista para almacenar los dispositivos
        print(f"Casa Inteligente '{nombre}' creada.")

    def agregar_dispositivo(self, dispositivo):
        """Agrega un dispositivo a la casa."""
        # Verificamos que sea un Dispositivo antes de agregarlo
        if isinstance(dispositivo, Dispositivo):
            self._dispositivos.append(dispositivo)
            print(f"Dispositivo '{dispositivo.id_dispositivo}' agregado a '{self.nombre}'.")
        else:
            print("Error: Solo se pueden agregar objetos que hereden de 'Dispositivo'.")

    def mostrar_todos(self):
        """Muestra el estado de todos los dispositivos en la casa."""
        print("-" * 30)
        print(f"Estado de Dispositivos en: {self.nombre}")
        print("-" * 30)
        if not self._dispositivos:
            print("No hay dispositivos registrados en la casa.")
            return

 for d in self._dispositivos:
            # Polimorfismo en acción:
            # Python llama al método mostrar_datos() de la clase
            # correcta (Luz, Camara, Sensor) automáticamente.
            d.mostrar_datos()
        print("-" * 30)

    def ejecutar_escena(self, nombre_escena):
        """
        Ejecuta una acción coordinada basada en el estado de los dispositivos.
        Ejemplo: "Si hay movimiento, enciende luces y graba."
        """
        print(f"\n>>> Ejecutando Escena: '{nombre_escena}' <<<")
        
        if nombre_escena == "alerta_movimiento":
            sensor_activado = None
            
            # 1. Buscar si algún sensor detectó movimiento
            for d in self._dispositivos:
                if isinstance(d, SensorMovimiento) and d.movimiento_detectado:
                    sensor_activado = d
                    break # Encontramos uno, salimos del bucle
            
            # 2. Si hubo detección, activar otros dispositivos
            if sensor_activado:
                print(f"ALERTA: Movimiento detectado por {sensor_activado.id_dispositivo}.")
                print("Acción: Encendiendo luces y activando cámaras...")
                
                for d in self._dispositivos:
                    # Si es una luz, encenderla al 100%
                    if isinstance(d, LuzInteligente):
                        d.encender()
                        d.intensidad = 100
                    
                    # Si es una cámara, iniciar grabación
                    if isinstance(d, CamaraSeguridad):
                        # La cámara debe estar encendida (standby) para grabar
                        if d.estado == "apagado":
                            d.encender() 
                        
                        d.iniciar_grabacion()
            else:
                print("Escena 'alerta_movimiento' verificada. No se detectó movimiento.")
        else:
            print(f"Escena '{nombre_escena}' no reconocida.")


# --- 4. SIMULACIÓN (Bloque principal) ---

# Esto asegura que el código solo se ejecute si el script es
# el archivo principal (y no si es importado por otro script).
if _name_ == "_main_":
    
    print("===== INICIANDO SIMULACIÓN DE CASA INTELIGENTE =====")
    
    # 1. Crear la casa
    mi_casa = CasaInteligente("Hogar Principal")
    print("=" * 50)

    # 2. Crear los 5 dispositivos
    luz_sala = LuzInteligente("LUZ-SALA-01")
    luz_cocina = LuzInteligente("LUZ-COCINA-01")
    sensor_puerta = SensorMovimiento("SEN-PUERTA-01")
    camara_entrada = CamaraSeguridad("CAM-ENTRADA-01")
    camara_patio = CamaraSeguridad("CAM-PATIO-01")

    # 3. Agregarlos a la casa
    print("\n===== Agregando Dispositivos =====")
    mi_casa.agregar_dispositivo(luz_sala)
    mi_casa.agregar_dispositivo(luz_cocina)
    mi_casa.agregar_dispositivo(sensor_puerta)
    mi_casa.agregar_dispositivo(camara_entrada)
    mi_casa.agregar_dispositivo(camara_patio)

    # 4. Mostrar estado inicial (todos deben estar apagados)
    mi_casa.mostrar_todos()

    # 5. Simular lecturas y encendidos
    print("\n===== Simulación de Uso Diario =====")
    
    # Encendemos los dispositivos que deben estar activos
    sensor_puerta.encender()
    camara_entrada.encender() # La ponemos en standby
    luz_sala.encender()
    luz_sala.intensidad = 20 # Luz tenue
    
    # Pausa para ver la simulación
    time.sleep(1) 

    # 6. Ejecutar escena SIN movimiento
    mi_casa.ejecutar_escena("alerta_movimiento")
    mi_casa.mostrar_todos()
    
    # 7. Simular detección de movimiento
    print("\n===== ¡Simulando Movimiento! =====")
    sensor_puerta.simular_movimiento()
    
    # Pausa para ver la simulación
    time.sleep(1)

    # 8. Ejecutar escena DE NUEVO (ahora sí debe reaccionar)
    mi_casa.ejecutar_escena("alerta_movimiento")
    
    # 9. Mostrar estado final
    print("\n===== Estado Final de la Casa =====")
    mi_casa.mostrar_todos()
    
    print("===== FIN DE LA SIMULACIÓN =====")
