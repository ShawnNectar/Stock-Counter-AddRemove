import dash
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
server = app.server

estoque = {
    "banana": 10,
    "maça": 14,
    "uva": 40,
}

app.layout = html.Div([
    html.H1('Stock'),
    html.P(id='banana-counter', children=f'Quantity of bananas: {estoque["banana"]}.'),
    html.Button('Adicionar 1 banana', id='banana-add'),
    html.Button('Subtrair 1 banana', id='banana-sub'),
    html.P(id='maça-counter', children=f'Quantity of apples: {estoque["maça"]}.'),
    html.Button('Adicionar 1 maçã', id='maça-add'),
    html.Button('Subtrair 1 maçã', id='maça-sub'),
    html.P(id='uva-counter', children=f'Quantity of grapes: {estoque["uva"]}.'),
    html.Button('Adicionar 1 uva', id='uva-add'),
    html.Button('Subtrair 1 uva', id='uva-sub'),
])

@app.callback(
    Output('banana-counter', 'children'),
    Input('banana-add', 'n_clicks'),
    Input('banana-sub', 'n_clicks'),
    State('banana-counter', 'children'))
def update_banana_counter(add_clicks, sub_clicks, current_text):
    global estoque
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'banana-add' in changed_id:
        estoque['banana'] += 1
    elif 'banana-sub' in changed_id:
        estoque['banana'] = max(estoque['banana'] - 1, 0)
    new_text = f'Quantity of bananas: {estoque["banana"]}.'
    return new_text

@app.callback(
    Output('maça-counter', 'children'),
    Input('maça-add', 'n_clicks'),
    Input('maça-sub', 'n_clicks'),
    State('maça-counter', 'children'))
def update_maca_counter(add_clicks, sub_clicks, current_text):
    global estoque
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'maça-add' in changed_id:
        estoque['maça'] += 1
    elif 'maça-sub' in changed_id:
        estoque['maça'] = max(estoque['maça'] - 1, 0)
    new_text = f'Quantity of apples: {estoque["maça"]}.'
    return new_text

@app.callback(
    Output('uva-counter', 'children'),
    Input('uva-add', 'n_clicks'),
    Input('uva-sub', 'n_clicks'),
    State('uva-counter', 'children'))
def update_uva_counter(add_clicks, sub_clicks, current_text):
    global estoque
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'uva-add' in changed_id:
        estoque['uva'] += 1
    elif 'uva-sub' in changed_id:
        estoque['uva'] = max(estoque['uva'] - 1, 0)
    new_text = f'Quantity of grapes: {estoque["uva"]}.'
    return new_text

if __name__ == '__main__':
    app.run_server(debug=True)