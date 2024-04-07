import requests

url = "http://localhost:8000/pacientes"
headers = {'Content-type': 'application/json'}

mi_paciente = {
    "ci": 1,
    "nombre": "Bart",
    "apellido": "Mendoza",
    "edad": 25,
    "genero": "Masculinno",
    "diagnostico": "Diabetes",
    "doctor": "Oscar Miranda"
}
response = requests.post(url, json=mi_paciente, headers=headers)
print(response.json())

mi_paciente2 = {
    "ci": 2,
    "nombre": "Javier",
    "apellido": "Lopez",
    "edad": 17,
    "genero": "Masculinno",
    "diagnostico": "Anemia",
    "doctor": "Pedro Perez"
}
response = requests.post(url, json=mi_paciente2, headers=headers)
print(response.json())