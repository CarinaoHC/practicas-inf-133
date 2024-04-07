import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"

# POST agrega un nuevo paciente por la ruta /pacientes
ruta_post = url + "pacientes"
nuevo_paciente = {
    "nombre": "Dayane",
    "apellcio": "Rivas",
    "edad": 20,
    "genero": "Femenino",
    "Diagnostico": "Diabetes",
    "Doctor": "Pedro Perez",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_paciente)
print(post_response.text)

# GET obtener a todos los pacientes por la ruta /pacientes
print("\nLISTAR PACIENTES")
ruta_get = url + "pacientes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# GET filtrando por ci con query params
print("\nPACIENTE POR CI")
ruta_get = url + "pacientes/2"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# GET Listar a los pacientes que tienen diagnostico de Diabetes
print("\n")
ruta_get = url + "pacientes/?diagnostico=Diabetes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)


# GET fListar a los pacientes que atiende el Doctor Pedro Pérez
print("\n")
ruta_get = url + "pacientes/?doctor=Pedro Perez"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# PUT actualiza un paciente por la ruta /pacientes/
print("\nACTUALIZAR PACIENTE")
ruta_update = url + "pacientes/2"
paciente_update = {
    "nombre": "Javier",
    "apellcio": "Lopez",
    "edad": 17,
    "genero": "Masculinno",
    "diagnostico": "Gastritis",
    "doctor": "Lucia Mendez"
}
put_response = requests.request(method="PUT", url=ruta_update, json=paciente_update)
print(put_response.text)

# DELETE elimina un paciente por la ruta /pacientes/
print("\nELIMINAR PACIENTE")
ruta_delete = url + "pacientes/1"
eliminar_response = requests.request(method="DELETE", url=ruta_delete)
print(eliminar_response.text)