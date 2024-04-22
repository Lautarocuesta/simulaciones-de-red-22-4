import time
#nodo
class Nodo:
  # Método __init__:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def eliminar_conexion(self, nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)

    def enviar_mensaje(self, mensaje):
        print(f"{self.nombre} enviando mensaje: {mensaje}")
        for conexion in self.conexiones:
            conexion.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} recibiendo mensaje: {mensaje}")


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

# Simulación de comunicación
servidor.enviar_mensaje("Hola a todos")

#segundos
time.sleep(5)  
print("Simulando desconexión y reconexión dinámica...")


servidor.eliminar_conexion(cliente1)
servidor.agregar_conexion(cliente1)
print("¡Hola de nuevo a todos!")