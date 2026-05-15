import json
import os

ARCHIVO = "vehiculos.json"

class Vehiculo:
    def __init__(self, placa, marca, modelo, anio):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio

    def get_placa(self):
        return self.__placa

    def mostrar_informacion(self):
        return {
            "tipo": "Vehiculo",
            "placa": self.__placa,
            "marca": self.__marca,
            "modelo": self.__modelo,
            "anio": self.__anio
        }

class Bus(Vehiculo):
    def __init__(self, placa, marca, modelo, anio, capacidad_pasajeros):
        super().__init__(placa, marca, modelo, anio)
        self.capacidad_pasajeros = capacidad_pasajeros

    def mostrar_informacion(self):
        datos = super().mostrar_informacion()
        datos["tipo"] = "Bus"
        datos["capacidad_pasajeros"] = self.capacidad_pasajeros
        return datos

class Taxi(Vehiculo):
    def __init__(self, placa, marca, modelo, anio, numero_licencia):
        super().__init__(placa, marca, modelo, anio)
        self.numero_licencia = numero_licencia

    def mostrar_informacion(self):
        datos = super().mostrar_informacion()
        datos["tipo"] = "Taxi"
        datos["numero_licencia"] = self.numero_licencia
        return datos

class Camion(Vehiculo):
    def __init__(self, placa, marca, modelo, anio, capacidad_carga):
        super().__init__(placa, marca, modelo, anio)
        self.capacidad_carga = capacidad_carga

    def mostrar_informacion(self):
        datos = super().mostrar_informacion()
        datos["tipo"] = "Camion"
        datos["capacidad_carga"] = self.capacidad_carga
        return datos

def cargar_vehiculos():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_vehiculos(vehiculos):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(vehiculos, archivo, indent=4, ensure_ascii=False)

def registrar_vehiculo():
    print("\n--- Registrar Vehículo ---")
    print("1. Bus")
    print("2. Taxi")
    print("3. Camión")

    opcion = input("Seleccione el tipo de vehículo: ")

    placa = input("Placa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    anio = input("Año: ")

    if opcion == "1":
        capacidad = int(input("Capacidad de pasajeros: "))
        vehiculo = Bus(placa, marca, modelo, anio, capacidad)

    elif opcion == "2":
        licencia = input("Número de licencia: ")
        vehiculo = Taxi(placa, marca, modelo, anio, licencia)

    elif opcion == "3":
        carga = float(input("Capacidad de carga en toneladas: "))
        vehiculo = Camion(placa, marca, modelo, anio, carga)

    else:
        print("Opción inválida.")
        return

    vehiculos = cargar_vehiculos()
    vehiculos.append(vehiculo.mostrar_informacion())
    guardar_vehiculos(vehiculos)

    print("Vehículo registrado correctamente.")


def consultar_vehiculos():
    print("\n--- Vehículos Registrados ---")

    vehiculos = cargar_vehiculos()

    if not vehiculos:
        print("No hay vehículos registrados.")
        return

    for vehiculo in vehiculos:
        print("\nTipo:", vehiculo["tipo"])
        print("Placa:", vehiculo["placa"])
        print("Marca:", vehiculo["marca"])
        print("Modelo:", vehiculo["modelo"])
        print("Año:", vehiculo["anio"])

        if vehiculo["tipo"] == "Bus":
            print("Capacidad de pasajeros:", vehiculo["capacidad_pasajeros"])

        elif vehiculo["tipo"] == "Taxi":
            print("Número de licencia:", vehiculo["numero_licencia"])

        elif vehiculo["tipo"] == "Camion":
            print("Capacidad de carga:", vehiculo["capacidad_carga"], "toneladas")


def buscar_vehiculo():
    print("\n--- Buscar Vehículo ---")
    placa = input("Ingrese la placa del vehículo: ")

    vehiculos = cargar_vehiculos()

    for vehiculo in vehiculos:
        if vehiculo["placa"] == placa:
            print("\nVehículo encontrado:")
            for clave, valor in vehiculo.items():
                print(f"{clave}: {valor}")
            return

    print("Vehículo no encontrado.")

def menu():
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE VEHÍCULOS =====")
        print("1. Registrar vehículo")
        print("2. Consultar vehículos")
        print("3. Buscar vehículo por placa")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_vehiculo()
        elif opcion == "2":
            consultar_vehiculos()
        elif opcion == "3":
            buscar_vehiculo()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")


menu()