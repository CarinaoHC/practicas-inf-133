# Importamos la biblioteca requests para hacer peticiones HTTP
import requests

# Definimos la URL del servicio al que vamos a hacer la petición
url = "http://localhost:8000/animales"

# Definimos los encabezados HTTP que vamos a enviar con la petición
headers = {"Content-Type": "application/json"}

animal_type = "Pez"
data = {"animal_type": animal_type}

# Hacemos una petición POST a la URL con los datos y encabezados definidos
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print("Error scheduling animal:", response.text)

animal_type = "ave"
data = {"animal_type": animal_type}

# Hacemos otra petición POST a la URL con los nuevos datos y los mismos encabezados
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print("Error scheduling animal:", response.text)
