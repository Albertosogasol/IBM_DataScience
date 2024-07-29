# Codigo para probar las http request en Python

import requests
import os
from PIL import Image
from IPython.display import IFrame

# URL a la que se hará la petición
url = 'https://www.ibm.com/'
r = requests.get(url)

# Los encabezados de la solicitud HTTP se obtienen:
print(r.request.headers)

"""
Los encabezados de la solicitud HTTP contienen información adicional enviada al servidor para proporcionar contexto sobre la solicitud. Aquí tienes una explicación de algunos encabezados comunes que podrías ver:

User-Agent: Identifica el cliente que realiza la solicitud (por ejemplo, el navegador o el programa).
Accept: Indica los tipos de contenido que el cliente puede procesar.
Accept-Encoding: Especifica los tipos de codificación de contenido que el cliente puede procesar.
Connection: Controla si la conexión permanece abierta después de que se ha completado la solicitud actual (por ejemplo, keep-alive).
"""

# El encabezado del cuerpo se obtiene:
print(r.request.body)
"""
Una solicitud GET en el protocolo HTTP no tiene cuerpo porque su propósito principal es solicitar datos de un servidor, no enviar datos al servidor
"""
