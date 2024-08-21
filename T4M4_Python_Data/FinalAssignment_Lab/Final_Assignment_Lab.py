import yfinance as yf
import pandas as pd
import matplotlib_inline
import json

# Cargamos los datos de apple usando yfinance
apple = yf.Ticker("AAPL")

# Leemos el archgivo json de prueba de apple que hemos descargado a mano
with open('T4M4\\FinalAssignment_Lab\\apple.json') as json_file:
    apple_info = json.load(json_file)

# Se obtiene información extrayendo del json la clave que nos interesa
print(f"El pais es: {apple_info['country']}")
print(f"Informacion: {apple_info['longBusinessSummary']}")

# Para extraer un historico con yfinance se usa el método history(). 
# Mediante el metodo period() se especifica el tiempo desde una fecha hasta la actual 
# The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max
apple_share_price_data = apple.history(period="max") # El metodo devuelve un DataFrame

# Le ponemos indices al DataFrame
apple_share_price_data.reset_index(inplace=True)
print(apple_share_price_data)

# Se grafican los valores (Solo funciona en Jupyter)
apple_share_price_data.plot(x="Date", y="Open")

# Para extraer los dividendos
apple.dividends

# Se pueden graficar los dividendos a lo largo del tiempo
apple.dividends.plot()

# Hacemos una prueba con AMD
amd = yf.Ticker("AMD")

# Sacamos el historico para guardarlo en un DataFrame
amd_share_price_data = amd.history(period="max")

# Activamos los indices
amd_share_price_data.reset_index(inplace=True)

# Imprimimos por pantalla
print(amd_share_price_data)