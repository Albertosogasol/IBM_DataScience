#Archivo para cargar datos de un csv en Python y transofmar los valores en unidades del Sistema Internacional

#Library import
import pandas as pd

#CSV path
csv_path = 'T4M4\height_weight.csv'

#Creating DataFrame
df = pd.read_csv(csv_path)

#Conversion units: 
# inches -> cm *2.54 
# pounds -> kg /.453592

# New col with converted values
inches_col = df.columns[1]
pounds_col = df.columns[2]
df['Height(cm)'] = df[inches_col] * 2.54
df['Weight(kg)'] = df[pounds_col] * 0.453592
print(df)

#New copied csv
df.to_csv('T4M4\height_weight_copy.csv', index=False)

# CSV to Python dictionary
df_dict = df.to_dict(orient='list')

# Filename
filename = 'T4M4\\new_dict_python.py'

# File content
file_content = f"""
# Este archivo fue generado automaticamente
df_dict = {df_dict}

# Imprimir el diccionario
print(df_dict)
"""

# Save file
with open(filename, 'w') as file:
    file.write(file_content)

print(f'Archivo {filename} creado con éxito.')