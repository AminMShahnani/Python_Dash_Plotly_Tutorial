from dash import Dash, html

app = Dash()

app.layout = html.Div([
    html.H1('World Happenes Dashboard'),
    html.P([
        'This Dashboard shows the happines score',
        html.Br(),
        html.A(
            'World Happiness Report Data Source',
            href='http://google.com',
            target='_blank'

        )
    ]),
])

if __name__ == "__main__" :
    app.run_server(debug=True)