from dash import Dash, html, dcc, dash_table
import plotly.graph_objects as go
import yfinance as yf

price=yf.Ticker('AAPL').history(period='1d', interval='15m').reset_index()

fig=go.Figure(data=go.Candlestick(
    x=price['Datetime'],
    open=price['Open'],
    high=price['High'],
    low=price['Low'],
    close=price['Close']
))


app = Dash()

app.layout = html.Div([
    html.H1('My Financial Dashboard'),
    dcc.Input(id='ticker-input',
              placeholder='Search for symbols from Yahoo Finance',
              style={'width':'50%'}),
    html.Button(id='submit-button', children='submit'),
    dcc.Graph(id='stock-graph', figure=fig),
    dash_table.DataTable(id='stock-data', 
                         data=price.tail(10).to_dict('records'))
])


if __name__ == '__main__':
    app.run_server(debug=True)