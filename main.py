from fastapi import FastAPI

app = FastAPI()

ESTUDIANTES = [
    {'id': 1, 'nombre': 'Didier', 'apellidos': 'Irias Mendez'}, 
    {'id': 2,'nombre': 'Alonso', 'Apellidos': 'Solano Soto'},
    {'id': 3,'nombre': 'Pedro', 'Apellidos': 'Mendez'}
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

# parametros de tipo path / endpoints
@app.get("/hola_mundo/{persona}")
async def hola_mundo(persona):
    return f'Hola {persona}'

@app.delete('/estudiantes/{id_estudiante}')
async def borrar_estudiante(id_estudiante):
    for estudiante in ESTUDIANTES:
        if estudiante.get('id') == int(id_estudiante):
            ESTUDIANTES.pop(ESTUDIANTES.index(estudiante))
            return {'message': 'estudiante eliminado', 'data': ESTUDIANTES}
    return {'error': 'El estudiante no existe'}


#return = devolver
#lowercase = Minuscula
#uppercase = Mayuscula
#endpoints
#hostname = http://127.0.0.1:8000 