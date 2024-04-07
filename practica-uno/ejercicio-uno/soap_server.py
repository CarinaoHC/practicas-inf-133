from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error"

dispatcher = SoapDispatcher(
    "ejercicio1-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Suma", suma, returns={"Resultado": int}, args={"x": int, "y": int}
)

dispatcher.register_function(
    "Resta", resta, returns={"Resultado": int}, args={"x": int, "y": int}
)

dispatcher.register_function(
    "Multiplicacion", multiplicacion, returns={"Resultado": int}, args={"x": int, "y": int}
)

dispatcher.register_function(
    "Division", division, returns={"Resultado": float}, args={"x": int, "y": int}
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()
