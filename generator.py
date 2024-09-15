# Para este proyecto necesitaremos la importación de 2 librerías de Python:
# - 'random': Para seleccionar caracteres aleatorios.
# - 'string': Para acceder a conjuntos de caracteres como letras y dígitos.
import random
import string

def generar_password(longitud=12):
    """
    Genera una contraseña aleatoria de una longitud especificada.
    
    Parámetros:
    longitud (int): La longitud de la contraseña a generar. Por defecto, es 12.
    
    Retorna:
    str: Una cadena de caracteres que representa la contraseña generada.
    """
    # Combinamos letras (mayúsculas y minúsculas) y dígitos para formar el conjunto de caracteres permitidos.
    caracteres = string.ascii_letters + string.digits
    
    # Creamos la contraseña seleccionando aleatoriamente caracteres del conjunto.
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    # Devolvemos la contraseña generada.
    return password

if __name__ == "__main__":
    # Genera una contraseña de 13 caracteres y la imprime en la consola.
    print(generar_password())

