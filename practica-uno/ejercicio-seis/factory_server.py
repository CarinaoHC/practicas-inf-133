from http.server import HTTPServer, BaseHTTPRequestHandler
import json
class JunglaAnimal:
    def __init__(self, nombre, especie, genero, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.genero = genero
        self.edad = edad
        self.peso = peso
        
    def jungla(self):
        return "Añadido con exito"

class Mamifero(JunglaAnimal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        
class Ave(JunglaAnimal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)

class Reptil(JunglaAnimal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)

class Anfibio(JunglaAnimal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)
        
class Pez(JunglaAnimal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__(nombre, especie, genero, edad, peso)

class JunglaFactory:
    def create_jungla_animal(self, animal_type, nombre, especie, genero, edad, peso):
        if animal_type == "mamifero":
            return Mamifero(nombre, especie, genero, edad, peso)
        elif animal_type == "ave":
            return Ave(nombre, especie, genero, edad, peso)
        elif animal_type == "reptil":
            return Reptil(nombre, especie, genero, edad, peso)
        elif animal_type == "anfibio":
            return Anfibio(nombre, especie, genero, edad, peso)
        elif animal_type == "pez":
            return Pez(nombre, especie, genero, edad, peso)
        else:
            raise ValueError("Tipo de animal no válido")


class JunglaRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/animales":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode("utf-8"))

            animal_type = request_data.get("animal_type")
            jungla_factory = JunglaFactory()
            jungla_animal = jungla_factory.create_jungla_animal(animal_type)

            response_data = {"message": jungla_animal.jungla()}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Ruta no encontrada")


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, JunglaRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()