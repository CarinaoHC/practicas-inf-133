from zeep import Client

client = Client("http://localhost:8000/")

x = 32
y = 3

resultado = client.service.Suma(x, y)
print(f" {x} + {y} : {resultado}")

resultado = client.service.Resta(x, y)
print(f" {x} - {y} : {resultado}")

resultado = client.service.Multiplicacion(x, y)
print(f" {x} * {y} : {resultado}")

resultado = client.service.Division(x, y)
print(f" {x} / {y} : {resultado}")
