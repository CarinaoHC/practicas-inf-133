from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Producto: Paciente
class Paciente:
    def __init__(self):
        self.ci = None
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.genero = None
        self.diagnostico = None
        self.doctor = None

    def __str__(self):
        return f"Ci: {self.ci}, Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad},Genero: {self.genero}, Diagnostico: {self.diagnostico}, Doctor: {self.doctor}"

# Builder: Constructor de pacientes
class PacienteBuilder:
    def __init__(self):
        self.paciente = Paciente()

    def set_ci(self, ci):
        self.paciente.ci = ci

    def set_nombre(self, nombre):
        self.paciente.nombre = nombre

    def set_apellido(self, apellido):
        self.paciente.apellido = apellido
    
    def set_edad(self, edad):
        self.paciente.edad = edad
        
    def set_genero(self, genero):
        self.paciente.genero = genero

    def add_diagnostico(self, diagnostico):
        self.paciente.diagnostico = diagnostico
    
    def set_doctor(self, doctor):
        self.paciente.doctor = doctor

    def get_paciente(self):
        return self.paciente

# Director: Hospital
class Hospital:
    def __init__(self, builder):
        self.builder = builder

    def create_patient(self, ci, nombre, apellido, edad, genero, diagnostico, doctor):
        self.builder.set_ci(ci)
        self.builder.set_nombre(nombre)
        self.builder.set_apellido(apellido)
        self.builder.set_edad(edad)
        self.builder.set_genero(genero)
        self.builder.set_diagnostico(diagnostico)
        self.builder.set_doctor(doctor)
        return self.builder.get_paciente()

# Manejador de solicitudes HTTP
class PacienteHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/pacientes':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            data = json.loads(post_data.decode('utf-8'))

            ci = data.get("ci", None)
            nombre = data.get("nombre", None)
            apellido = data.get("apellido", None)
            edad = data.get("edad", None)
            genero = data.get("genero", None)
            diagnostico = data.get("diagnostico", None)
            doctor = data.get("doctor", None)

            builder = PacienteBuilder()
            hospital = Hospital(builder)

            paciente = hospital.create_patient(ci, nombre, apellido, edad, genero, diagnostico, doctor)
        
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            response = {
                'ci': paciente.ci,
                'nombre': nombre,
                'apellido': apellido,
                'edad': edad,
                'genero': genero,
                'diagnostico': diagnostico,
                'doctor': doctor
                }

            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=PacienteHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()