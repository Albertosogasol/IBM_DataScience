# Importacion de librerias
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Se desactivan warnings
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Se van a extraer datos de bolsa de Netflix directamente de la pagina de YahooFinance. Para ello se utilizará Web Scrap
# URL: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html
# En esta web hay una tabla que contiene columnas: Date, Open, High, Low, Close, Volume

#Pasos a seguir para extraer los datos:
"""
1. Enviar una solicitud HTTP a la página web usando la biblioteca requests.
2. Analizar el contenido HTML de la página web usando BeautifulSoup.
3. Identificar las etiquetas HTML que contienen los datos que deseas extraer.
4. Utilizar los métodos de BeautifulSoup para extraer los datos de las etiquetas HTML.
5. Imprimir los datos extraídos.
"""

# URL
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

# Extracción del contenido HTML de la solicitud .get()
data = requests.get(url).text

# Creacion de objeto de BeautifulSoup
soup = BeautifulSoup(data, 'html.parser') # El segundo argumento es opcional. Elige si es html o xml. El predeterminado es html

# Creacion de DataFrame 
# Para este caso elegimos como columnas: Date, Open, High, Low, Close, Volume

netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# Uso de BeautifulSoup para extaer datos
# Se usan los metodos find() y find_all() para localizar el cuerpo de la table asi como las filas en el HTML
# .find() devuelve una etiqueta en particular
# .find_all() devuelve una lista con todas las coincidencias en el HTML
# Proceso:
# Se aisla el cuerpo de la tabla que contiene toda la información
# Se itera a través de cada fila para encontrar los valores de cada una

"""
Trabajando con tablas HTML

Estos son los siguientes tags que se utilizan al crear tablas HTML.

* <table>: Este tag es el tag raíz usado para definir el inicio y el fin de la tabla. Todo el contenido de la tabla está contenido dentro de estos tags.

* <tr>: Este tag se usa para definir una fila de la tabla. Cada fila de la tabla se define dentro de este tag.

* <td>: Este tag se usa para definir una celda de la tabla. Cada celda de la tabla se define dentro de este tag. Puedes especificar el contenido de la celda entre las etiquetas de apertura y cierre <td>.

* <th>: Este tag se usa para definir una celda de encabezado en la tabla. La celda de encabezado se usa para describir el contenido de una columna o fila. Por defecto, el texto dentro de un tag <th> es negrita y está centrado.

* <tbody>: Este es el contenido principal de la tabla, que se define usando el tag <tbody>. Contiene una o más filas de elementos <tr>.
"""

# Explicación del bucle siguiente:
"""
1. Sobre el objeto soup proveniente de la petición y del parse html se realizan busquedas
2. Se busca la primera etiqueta <tbody> que corresponde al cuerpo de la tabla
3. Sobre esa tabla se busca cada etiqueta <tr> que corresponde a cada fila de la tabla
4. La variable 'col' corresponde a una lista con los valores de cada fila. Se realiza una busqueda de cada celda dentro de esa fila 'row', que corresponde a la etiqueta <td>
5. A cada variable se le asigna el valor correspondiente

"""

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    # Se añade cada dato a la fila de la columna
    netflix_data = pd.concat([netflix_data,pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)

# Se imprimen los primeros datos de la tabla
print(f"Los datos mediante BeautifuldataSoup son:\n{netflix_data.head()}")

#############################################

# Tambien se puede usar la librería Pandas para extraer datos del HTML

# Se usa la función .read_html()
read_html_pandas_data = pd.read_html(url)

# Tambien se podría convertir el objeto beautifulsoup a string
#read_html_pandas_data = pd.read_html(str(soup))

# Se elige la tabla. En este caso solo hay una
netflix_dataframe = read_html_pandas_data[0]

# Se muestran los primeros datos
print(f"Los datos mediante pandas son:\n{netflix_dataframe.head()}")