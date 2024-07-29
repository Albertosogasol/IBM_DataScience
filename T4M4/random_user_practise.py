# Codigo para probar la API de usuarios random

from randomuser import RandomUser
import pandas as pd
import os

# Funcion para crear DataFrame
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10000):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)    

# Creacion de un objeto de tipo RandomUser
r = RandomUser()

# Generacion de n usuarios aleatorios
some_list = r.generate_users(5)

for user in some_list:
    print(user.get_full_name()," ",user.get_email()," ",user.get_zipcode())

df1 = pd.DataFrame(get_users()) 

print(df1)

#Guardamos en un csv
path = 'T4M4\\RandomUsers.csv'

df1.to_csv(path)