# Código correspondiente a la tarea "practice_project"
#Enunciado:
"""
An international firm that is looking to expand its business in different countries across the world has recruited you. You have been hired as a junior Data Engineer and are tasked with creating a script that can extract the list of the top 10 largest economies of the world in descending order of their GDPs in Billion USD (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF). 

The required data seems to be available on the URL mentioned below:

https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29

"""

# Objectives

"""
After completing this lab you will be able to:

- Use Webscraping to extract required information from a website.
- Use Pandas to load and process the tabular data as a dataframe.
- Use Numpy to manipulate the information contatined in the dataframe.
- Load the updated dataframe to CSV file.

"""
##############################################################################
##############################################################################

#Library import
import numpy as np
import pandas as pd

# URL
url_path = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Main table in url --> 3

# Import tables from URL
tables = pd.read_html(url_path)

# Extract table 3
df = tables[3]

# Change columns headers with numbers from 0 to shape - 1 
df.columns = range(df.shape[1])

# Extract columns 0 and 2
df = df[[0,2]]

# Filter with top 10 economies in the world
df = df.iloc[1:11,:] #Los dos puntos de después de la coma seleccionan todas las columas

# Assign column headers
df.columns = ['Country', 'GDP (Million USD)']
print(f"Top 10 economies in world based on Wikipedia webpage are: \n\n{df}")

# Exercise 2
"""
Modify the GDP column of the DataFrame, converting the value available in Million USD to Billion USD. Use the `round()` method of Numpy library to round the value to 2 decimal places. Modify the header of the DataFrame to `GDP (Billion USD)`.
"""

# Datatype of 'GDP' column to integer
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(float) #Se modifica a tipo entero

#Convert MIllion USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']] / 1000

# Use numpy.round() method to round the value to 2 decimal places.
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)

#Rename columns header
df.rename(columns= {'GDP (Million USD)' : 'GDP (Billion USD)'})

print(f"Top 10 economies in world based on Wikipedia webpage are: \n\n{df}")

