import os
import random
import string

# Crea un número n de archivos con letras aleatorias en su interior. 
# La ruta del archivo viene definida en filename
def create_random_letter_file(file_number):
    # Generar 1000 letras aleatorias
    random_letters = ''.join(random.choices(string.ascii_letters, k=100000))
    
    # Crear el nombre del archivo
    #filename = f'file_{file_number}.py'
    filename = f'T4M3_Python_Fundamentals//pruebas//outputs//file_{file_number}.py'  # Cambia '/ruta/deseada/' por la ruta que prefieras

    
    # Escribir las letras aleatorias como comentario en el archivo
    with open(filename, 'w') as file:
        file.write(f'# {random_letters}')
    
    print(f'Archivo {filename} creado con éxito.')

def main():
    # Pedir al usuario cuántos archivos crear
    try:
        N = int(input("¿Cuántos archivos deseas crear? "))
        if N <= 0:
            print("Por favor, ingresa un número positivo.")
            return
        
        # Crear N archivos
        for i in range(1, N + 1):
            create_random_letter_file(i)
    
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
