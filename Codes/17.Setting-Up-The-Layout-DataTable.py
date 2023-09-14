from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


electricity = pd.read_csv('../CSV_Files/electricity.csv')

year_min = electricity['Year'].min()
year_max = electricity['Year'].max()


avg_price_electricity = electricity \
                        .groupby('US_State')['Residential Price'] \
                        .mean() \
                        .reset_index() 
map_fig = px.choropleth(avg_price_electricity,
                        locations='US_State', 
                        locationmode='USA-states',
                        color='Residential Price',
                        scope='usa',
                        color_continuous_midpoint=1)

app = Dash(external_stylesheets=[dbc.themes.SOLAR])

app.layout= html.Div([
    html.H1('Electricity Prices By US State'),
    dcc.RangeSlider(id='year-slider',
                    min=year_min,
                    max=year_max,
                    value=[year_min, year_max],
                    marks={i:str(i) for i in range(year_min, year_max+1)}),
    dcc.Graph(id='map-graph', figure=map_fig),
    dash_table.DataTable(id='price-info',
                         data=electricity.to_dict('records'))
])

if __name__ == '__main__' :
    app.run_server(debug=True)