# Codigo para practicar CRUD en SQLite a través de Python

# Usamos SQLite
import sqlite3

# Creacion del objeto de conexion
conn = sqlite3.connect(r'T6M4\SQL_Python\PRACTISE_DATABASE.db')

# Objeto cursor
cursor_obj = conn.cursor()

# Si la tabla existe se elimina antes de volver a crearla. Con esto evitamos errores
cursor_obj.execute("DROP TABLE IF EXISTS People")

# Creacion de la tabla
create_table = "CREATE TABLE People (ID INTEGER PRIMARY KEY NOT NULL, NAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), ZIP VARCHAR(10))"

cursor_obj.execute(create_table)

# Añadir datos
add_data = "INSERT INTO People (NAME, LNAME, CITY, ZIP) VALUES ('Alberto', 'Gonzaga', 'Zaragoza', '50005')"

cursor_obj.execute(add_data)

# Recuperar informacion
view_data = "SELECT * FROM People"

cursor_obj.execute(view_data)

print("Todos los datos son: ")

all_data = cursor_obj.fetchall()

for row_all in all_data:
    print(row_all)

# Importar los datos en Pandas
import pandas as pd

# Se añaden los datos a un dataframe
df_sql_read = "SELECT * FROM People"

df = pd.read_sql_query(df_sql_read, conn)

print(df)

