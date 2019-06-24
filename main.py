import json_modifier as jm
from flask import Flask, render_template, jsonify


app = Flask(__name__, template_folder='')


@app.route('/')
def hello():

    data = {}
    sidebar_data = jm.get_jsons_map()

    data["sidebar"] = sidebar_data

    return render_template('index.html', data=data)


@app.route('/<string:id>')
def send_portfolio(id=id):

    json_path = jm.get_jsons_map()[id]
    portfolio_mapper = jm.PortfolioTreeMapper()

    return jsonify(portfolio_mapper.get_json(json_path))


if __name__ == '__main__':
    app.run()
