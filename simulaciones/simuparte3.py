import random
import time  
#nodo
class Nodo:
     # Método __init__:
    def __init__(self, nombre, capacidad_buffer=5):
        self.nombre = nombre
        self.conexiones = []
        self.buffer = []
        self.capacidad_buffer = capacidad_buffer

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def eliminar_conexion(self, nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)

    def enviar_mensaje(self, mensaje):
        if len(self.buffer) < self.capacidad_buffer:
            print(f"{self.nombre} enviando mensaje: {mensaje}")
            for conexion in self.conexiones:
                if random.random() < 0.3:  # Probabilidad de pérdida es del 0.3
                    print(f"¡Pérdida! Mensaje perdido{self.nombre} a {conexion.nombre}")
                else:
                    conexion.recibir_mensaje(mensaje)
        else:
            print(f"{self.nombre} está congestionado. Mensaje \"{mensaje}\" almacenado en el buffer.")
            self.buffer.append(mensaje)

    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} recibiendo mensaje: {mensaje}")
            if self.buffer:
            self.procesar_buffer()

    def procesar_buffer(self):
        print(f"Procesando buffer en {self.nombre}:")
        while self.buffer:
            mensaje = self.buffer.pop(0)  
            print(f"Mensaje \"{mensaje}\" procesado desde el buffer en {self.nombre}.")


# Creación de nodos
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente1")
cliente2 = Nodo("Cliente2")
cliente3 = Nodo("Cliente3")

# Establecimiento de conexiones
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)
cliente1.agregar_conexion(servidor)
cliente2.agregar_conexion(servidor)
cliente3.agregar_conexion(servidor)

# metodo de comunicacion
for i in range(1, 6):
    mensaje = f"Mensaje {i}"
    servidor.enviar_mensaje(mensaje)

# Simulación de desconexión y reconexión dinámica
time.sleep(2) 
print("Simulando desconexión y reconexión dinámica...")


servidor.eliminar_conexion(cliente1)
servidor.agregar_conexion(cliente1)
print("¡Hola a todos!")
