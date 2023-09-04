from dash import Dash, html

app = Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P([
        'This Dashboard shows the happiness score',
        html.Br(),
        html.A(
            'World Happiness Report Data Source',
            href='https://worldhappiness.report',
            target='_blank'

        )
    ]),
])

if __name__ == "__main__" :
    app.run_server(debug=True)