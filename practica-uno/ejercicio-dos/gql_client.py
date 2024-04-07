import requests

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple
query_lista = """
{
        plantas{
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
"""

# Definir la consulta GraphQL para crear nueva planta
query_crear = """
mutation {
        crearPlanta(nombre: "Eucalipto", especie: "Arbol", edad: 12, altura: 36.7, frutos: false) {
            planta {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

# Lista de todas las plantas
print("\nLISTAR PLANTAS :")
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL para buscar plantas por especie
query_buscarEspecie = """
    {
        plantaPorEspecie(especie: "Arbol"){
            nombre
            especie
        }
    }
"""
response = requests.post(url, json={'query': query_buscarEspecie})
print(response.text)

# Definir la consulta GraphQL para buscar plantas que tienen frutos
query_buscarFrutos = """
    {
        plantaPorFruto(frutos: true){
            nombre
        }
    }
"""
response = requests.post(url, json={'query': query_buscarFrutos})
print(response.text)

# Definir la consulta GraphQL para actualizar una planta
query_actualizar = """
mutation {
        updatePlanta(id: 2, nombre: "Girasol", especie: "Helianthus annuus", edad: 15, altura: 63, frutos: false) {
            planta {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""
response_mutation_ac = requests.post(url, json={'query': query_actualizar})
print(response_mutation_ac.text)

# Definir la consulta GraphQL para eliminar una planta
query_eliminar = """
mutation {
        deletePlanta(id:1) {
            planta{
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)

# Lista de todas las plantas
print("\nLISTAR PLANTAS :")
response = requests.post(url, json={'query': query_lista})
print(response.text)