"""STATEMENT:
(English)
In this assignment, you are a Data Analyst working at a Real Estate Investment Trust. The Trust would like to start investing in Residential real estate. You are tasked with determining the market price of a house given a set of features. You will analyze and predict housing prices using attributes or features such as square footage, number of bedrooms, number of floors, and so on. This is a template notebook; your job is to complete the ten questions. Some hints to the questions are given.

(Spanish)
En esta tarea, usted es un analista de datos que trabaja en un fondo de inversión inmobiliaria. El Trust quiere empezar a invertir en inmuebles residenciales. Se le encarga determinar el precio de mercado de una vivienda dado un conjunto de características. Analizará y predecirá los precios de las viviendas utilizando atributos o características como los metros cuadrados, el número de dormitorios, el número de plantas, etc. En el laboratorio se le proporciona un cuaderno plantilla; su trabajo consiste en completar las diez preguntas. En el cuaderno de plantilla se dan algunas pistas para las preguntas.
"""

# Packgages installation. Uncomment if necessary
#!pip install -qy pandas==1.3.4 numpy==1.21.4 seaborn==0.9.0 matplotlib==3.5.0 scikit-learn==0.20.1
#!pip install -U scikit-learn
#!pip install seaborn

# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
#%matplotlib inline

def LineJump(question_number):
    print()
    print(f"QUESTION {question_number}:")
    print(40*"-")
    print()
# URL to download csv file:
#filepath='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
# Change filename to: "housing.csv"

# Load CSV
#filepath='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
filepath = r"T7M6_FinalAssignment\Project\housing.csv"
df = pd.read_csv(filepath)

# Display the first 5 columns of the dataframe
df.head()
print(df.head())

# QUESTION 1:
# Display the data types of each column using the function dtypes. Take a screenshot of your code and output. You will need to submit the screenshot for the final project. 
LineJump(1)

print(df.dtypes)


# QUESTION 2:
# Drop the columns "id" and "Unnamed: 0" from axis 1 using the method dropt(), then use the method describe() to obtain a statistical summary of the data. Make sure the inplace parameter is set to True.
LineJump(2)










