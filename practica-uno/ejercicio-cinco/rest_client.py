import requests
# Consultando a un servidor RESTful
url = "http://localhost:8000/"

# POST agrega un nuevo animal por la ruta /animales
ruta_post = url + "animales"
nuevo_animal = {
    "nombre": "Confi",
    "especie": "Conejo",
    "genero": "Macho",
    "edad": 1,
    "peso": 9,
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_animal)
print(post_response.text)

# GET obtener a todos los animales por la ruta /animales
print("\nLISTAR ANIMALES")
ruta_get = url + "animales"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# GET Buscar animales por especie
print("\n")
ruta_get = url + "animales/?especie=Gato"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# GET Buscar animales por género
print("\n")
ruta_get = url + "animales/?genero=Macho"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# PUT actualiza un animal por la ruta /animales
print("\n")
ruta_update = url + "animales/3"
update_animal = {
    "nombre": "Confi",
    "especie": "Liebre",
    "genero": "Hembra",
    "edad": 2,
    "peso": 13,
}
post_response = requests.request(method="PUT", url=ruta_update, json=update_animal)
print(post_response.text)

# DELETE elimina un animal por la ruta /animales
print("\n")
ruta_delete = url + "animales/1"
post_response = requests.request(method="DELETE", url=ruta_delete)
print(post_response.text)
