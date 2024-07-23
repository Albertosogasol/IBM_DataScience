# Este programa se usa para hacer pruebas de lectura y escritura de archivos de texto con Python

filename = "T4M4\ExampleFile.txt"


#Ahora probamos a escribir
with open(filename, "w") as file2: 
    file_write = file2.write("Esta línea es añadida\n")

#Volvemos a leer
with open(filename,"r") as file1:
    file_read = file1.readlines()
    for line in file_read:
        print(line)

#Probamos a añadir al final del archivo mediante append
with open(filename, "a") as file3: 
    for i in range(0,100):
        file3.write(f"Esto es la línea añadida {i}\n")
