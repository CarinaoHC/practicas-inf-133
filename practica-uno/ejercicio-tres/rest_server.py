from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse, parse_qs

pacientes = [
    {
        "ci": 1,
        "nombre": "Bart",
        "apellcio": "Mendoza",
        "edad": 25,
        "genero": "Masculinno",
        "diagnostico": "Diabetes",
        "doctor": "Oscar Miranda"
    },
    {
        "ci": 2,
        "nombre": "Javier",
        "apellcio": "Lopez",
        "edad": 17,
        "genero": "Masculinno",
        "diagnostico": "Anemia",
        "doctor": "Pedro Perez"
    },
]


class PacientesService:
    @staticmethod
    def find_patient(ci):
        return next(
            (paciente for paciente in pacientes if paciente["ci"] == ci),
            None,
        )

    @staticmethod
    def filter_patients_by_doctor(doctor):
        return [
            paciente for paciente in pacientes if paciente["doctor"] == doctor
        ]

    @staticmethod
    def filter_patients_by_diagnostico(diagnostico):
        print("HOLA BEBE")
        return [
            paciente for paciente in pacientes if paciente["diagnostico"] == diagnostico
        ]


    @staticmethod
    def add_patient(data):
        data["ci"] = len(pacientes) + 1
        pacientes.append(data)
        return pacientes

    @staticmethod
    def update_patient(ci, data):
        paciente = PacientesService.find_patient(ci)
        if paciente:
            paciente.update(data)
            return pacientes
        else:
            return None

    @staticmethod
    def delete_patients():
        pacientes.clear()
        return pacientes
    
    @staticmethod
    def delete_patient(ci):
        paciente = PacientesService.find_patient(ci)
        if paciente:
            paciente.clear()
            return pacientes
        else:
            return None



class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))


class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if parsed_path.path == "/pacientes":
            HTTPResponseHandler.handle_response(self, 200, pacientes)
        elif self.path.startswith("/pacientes/"):
            ci = int(self.path.split("/")[-1])
            paciente = PacientesService.find_patient(ci)
            if paciente:
                HTTPResponseHandler.handle_response(self, 200, [paciente])
            else:
                HTTPResponseHandler.handle_response(self, 204, [])
        elif "diagnostico" in query_params:
            diagnostico = query_params["diagnostico"][0]
            pacientes_filtrados = PacientesService.filter_patients_by_diagnostico(
                diagnostico
            )
            if pacientes_filtrados != []:
                HTTPResponseHandler.handle_response(self, 200, pacientes_filtrados)
            else:
                HTTPResponseHandler.handle_response(self, 204, [])
        elif "doctor" in query_params:
            doctor = query_params["doctor"][0]
            pacientes_filtrados = PacientesService.filter_patients_by_doctor(
                doctor
            )
            if pacientes_filtrados != []:
                HTTPResponseHandler.handle_response(self, 200, pacientes_filtrados)
            else:
                HTTPResponseHandler.handle_response(self, 204, [])    
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_POST(self):
        if self.path == "/pacientes":
            data = self.read_data()
            pacientes = PacientesService.add_patient(data)
            HTTPResponseHandler.handle_response(self, 201, pacientes)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_PUT(self):
        if self.path.startswith("/pacientes/"):
            ci = int(self.path.split("/")[-1])
            data = self.read_data()
            pacientes = PacientesService.update_patient(ci, data)
            if pacientes:
                HTTPResponseHandler.handle_response(self, 200, pacientes)
            else:
                HTTPResponseHandler.handle_response(
                    self, 404, {"Error": "paciente no encontrado"}
                )
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_DELETE(self):
        if self.path == "/pacientes":
            pacientes = PacientesService.delete_patients()
            HTTPResponseHandler.handle_response(self, 200, pacientes)
        elif self.path.startswith("/pacientes/"):
            ci = int(self.path.split("/")[-1])
            paciente = PacientesService.delete_patient(ci)
            if paciente:
                HTTPResponseHandler.handle_response(self, 200, [paciente])
            else:
                HTTPResponseHandler.handle_response(self, 204, [])
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servcior web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servcior web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()