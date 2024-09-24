from fastapi import FastAPI

app = FastAPI()

ESTUDIANTES = [
    {'nombre': 'Didier', 'apellidos': 'Irias Mendez'}, 
    {'nombre': 'Alonso', 'Apellidos': 'Solano Soto'},
    {'nombre': 'Pedro', 'Apellidos': 'Mendez'}
    ]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/alonso")
async def root():
    return {"message": "Hola Alonso"}

@app.get("/estudiantes")
async def traer_estudiante():
    return ESTUDIANTES

#parametros de tipo path / url
@app.get("/estudiantes/{nombre_estudiante}")
async def mostrar_estudiante(nombre_estudiante):
    for estudiante in ESTUDIANTES:
        if estudiante.get('nombre').lower() == nombre_estudiante.lower():
            return estudiante
    return {'error': 'El estudiante no existe'}

#return = devolver
#lowercase = Minuscula
#uppercase = Mayuscula
#endpoints
#hostname = http://127.0.0.1:8000 