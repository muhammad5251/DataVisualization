import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

data_url = "https://raw.githubusercontent.com/muhammad5251/DataVisualization/data/aggregate_data_2023-01-08.csv"
data = pd.read_csv(data_url)
data3 = data[['PARLIAMENTARY NAME', 'TOTAL ELECTORS', 'MALAY (%)', 'CHINESE (%)']]
data3 = data3.sort_values('TOTAL ELECTORS', ascending=False)

fig_bar = px.bar(data3, x='PARLIAMENTARY NAME', y='TOTAL ELECTORS')

fig_box = px.box(data3, x='TOTAL ELECTORS', title='Box Plot of Total Electors by Constituency')

# Given data
data = {
    'PARLIAMENTARY NAME': ['BANGI', 'KOTA RAJA', 'DAMANSARA', 'SUBANG', 'TEBRAU', 'ISKANDAR PUTERI',
                           'KLANG', 'GOMBAK', 'PASIR GUDANG', 'PETALING JAYA'],
    'TOTAL ELECTORS': [303430, 244712, 239103, 230940, 223301, 222437, 208913, 206744, 198485, 195148],
    'MALAY (%)': [48.43, 39.81, 20.66, 26.25, 44.96, 36.27, 26.65, 69.94, 46.13, 46.15],
    'CHINESE (%)': [36.96, 29.68, 66.14, 54.04, 38.77, 47.22, 52.77, 10.86, 36.17, 29.56]
}

# Create the DataFrame
data3 = pd.DataFrame(data)

# Create the pie chart for Malay population
fig_pie_malay = px.pie(data3, values='MALAY (%)', names='PARLIAMENTARY NAME', title='Malay Population (%) by Constituency')

# Create the pie chart for Chinese population
fig_pie_chinese = px.pie(data3, values='CHINESE (%)', names='PARLIAMENTARY NAME', title='Chinese Population (%) by Constituency')

app.layout = html.Div([
    html.H1("Hasanuddin Assignment 3"),
    
    dcc.Graph(figure=fig_bar),
    
    dcc.Graph(figure=fig_box),
    
    dcc.Graph(figure=fig_pie_malay),
    
    dcc.Graph(figure=fig_pie_chinese)
])

if __name__ == '__main__':
    app.run_server(debug=True)
