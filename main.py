import json_modifier as jm
from flask import Flask, render_template, jsonify


app = Flask(__name__, template_folder='')


@app.route('/')
def index():

    data = {}
    sidebar_data = jm.get_list_portfolio_id_name()

    data["sidebar"] = sidebar_data

    return render_template('index.html', data=data)


@app.route('/<string:id>')
def send_portfolio(id=id):

    json_path = jm.get_list_portfolio_id_name()[id]

    return jsonify(get_portfolio(json_path))


def get_portfolio(json_path):
    portfolio_mapper = jm.PortfolioTreeMapper()

    try:
        return portfolio_mapper.get_json(json_path)
    except ValueError:
        return {
            'text': {'name': 'Sorry! Error with portfolio file!\nWrong file:{}'.format(json_path)},
            'children': []
        }
    except KeyError:
        return {
            'text': {'name': 'Sorry! Portfolio {} has not expected json keys'.format(json_path)},
            'children': []
        }


if __name__ == '__main__':
    app.run(host='0.0.0.0')
