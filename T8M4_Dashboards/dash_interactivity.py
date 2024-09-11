# Import required libraries
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Read the airline data into the pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str}) # dtype fuerza a que ciertas columnas se interpreten como cadenas de caracteres.
# Create a dash application
app = dash.Dash(__name__) # inicializa la aplicación Dash.
                               
# El layout define la estructura y los componentes visuales de la aplicación. Aquí se incluyen varios elementos:
# html.H1: Un título principal que dice "Airline Performance Dashboard", con estilos personalizados (alineado al centro, color y tamaño de fuente).
# html.Div: Contiene un campo de entrada para el año (dcc.Input), donde el usuario puede escribir un año (por defecto es 2010).
# dcc.Graph: Un contenedor donde se mostrará el gráfico de líneas con el id 'line-plot'.
app.layout = html.Div(children=[ html.H1('Airline Performance Dashboard',style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.Div(["Input Year: ", dcc.Input(id='input-year', value='2010', 
                                type='number', style={'height':'50px', 'font-size': 35}),], 
                                style={'font-size': 40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='line-plot')),
                                ])

# add callback decorator
# Aquí se define una callback que actualiza el gráfico cuando el usuario introduce un nuevo año en el campo de entrada.
# Output: La propiedad figure del componente 'line-plot' será actualizada con el gráfico generado.
# Input: La función se ejecuta cada vez que cambia el valor del componente input-year.
@app.callback( Output(component_id='line-plot', component_property='figure'),
               Input(component_id='input-year', component_property='value'))

# Add computation to callback function and return graph
# La función filtra los datos del DataFrame original para seleccionar solo las filas correspondientes al año ingresado por el usuario.
# Agrupación y cálculo de promedios: Luego agrupa los datos por mes (Month) y calcula el retraso promedio de llegada (ArrDelay) para cada mes.
# Creación del gráfico de líneas: Se utiliza go.Figure para crear un gráfico de líneas usando plotly. La variable fig contiene el gráfico, con los meses en el eje x y el retraso promedio en el eje y.
# Actualización del diseño del gráfico: El gráfico se personaliza con un título, etiquetas para los ejes, y el color de la línea.
def get_graph(entered_year):
    # Select 2019 data
    df =  airline_data[airline_data['Year']==int(entered_year)]
    
    # Group the data by Month and compute average over arrival delay time.
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()