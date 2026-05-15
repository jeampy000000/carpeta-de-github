import json

class Usuario:
    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo

    # Getters
    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    # Método mostrar perfil
    def mostrar_perfil(self):
        return f"""
        ID: {self.__identificacion}
        Nombre: {self.__nombre}
        Correo: {self.__correo}
        """

    # Convertir a diccionario
    def to_dict(self):
        return {
            "identificacion": self.__identificacion,
            "nombre": self.__nombre,
            "correo": self.__correo
        }


class Estudiante(Usuario):

    def __init__(self, identificacion, nombre, correo, carrera):
        super().__init__(identificacion, nombre, correo)
        self.__carrera = carrera

    # Polimorfismo
    def mostrar_perfil(self):
        return f"""
        ===== PERFIL ESTUDIANTE =====
        ID: {self.get_identificacion()}
        Nombre: {self.get_nombre()}
        Correo: {self.get_correo()}
        Carrera: {self.__carrera}
        """

    def to_dict(self):
        datos = super().to_dict()
        datos["tipo"] = "Estudiante"
        datos["carrera"] = self.__carrera
        return datos


class Profesor(Usuario):

    def __init__(self, identificacion, nombre, correo, especialidad):
        super().__init__(identificacion, nombre, correo)
        self.__especialidad = especialidad

    # Polimorfismo
    def mostrar_perfil(self):
        return f"""
        ===== PERFIL PROFESOR =====
        ID: {self.get_identificacion()}
        Nombre: {self.get_nombre()}
        Correo: {self.get_correo()}
        Especialidad: {self.__especialidad}
        """

    def to_dict(self):
        datos = super().to_dict()
        datos["tipo"] = "Profesor"
        datos["especialidad"] = self.__especialidad
        return datos

usuarios = []

usuarios.append(
    Estudiante("101", "Carlos Perez", "carlos@gmail.com", "Ingeniería")
)

usuarios.append(
    Estudiante("102", "Ana Torres", "ana@gmail.com", "Medicina")
)

usuarios.append(
    Profesor("201", "Luis Gómez", "luis@gmail.com", "Matemáticas")
)

usuarios.append(
    Profesor("202", "Marta Ruiz", "marta@gmail.com", "Programación")
)


datos = []

for usuario in usuarios:
    datos.append(usuario.to_dict())

with open("usuarios.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)

print("Usuarios guardados correctamente.\n")

buscar_id = input("Ingrese la identificación del usuario: ")

encontrado = False

for usuario in usuarios:

    if usuario.get_identificacion() == buscar_id:

        print("\nUsuario encontrado:")
        print(usuario.mostrar_perfil())

        encontrado = True
        break

if encontrado == False:
    print("\nUsuario no encontrado.")