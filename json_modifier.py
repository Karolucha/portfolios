import os
import json


def get_all_jsons(dir="portfolio_data"):
    jsons = []

    for filename in os.listdir(dir):
        if filename.endswith(".json"):
            jsons.append(os.path.join(dir, filename))

    return jsons


def get_json_title(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
        return data["name"]


def get_jsons_map(dir="portfolio_data"):
    jsons = get_all_jsons(dir)
    map = {}
    for i, name in enumerate(jsons):
        map["portfolio_" + str(i)] = name
    return map


class PortfolioTreeMapper:

    def get_json(self, json_path):
        with open(json_path) as json_file:
            try:
                data = json.load(json_file)
            except ValueError:
                return {
                'text': {'name': 'Sorry! Error with portfolio file!\nWrong file:{}'.format(json_path)},
                'children': []
            }

            full_portfolio = {
                'text': {'name': data['name']},
                'children': self.get_portfolio(data['children']) or self.get_empty_child()
            }

        return full_portfolio

    def get_empty_child(self):
        return {
                'text': {'name': 'No children in this portfolio'},
                'children': []
            }
    def get_portfolio(self, portfolio_children):
        children = []
        for portfolio_detail in portfolio_children:
            print(portfolio_detail)
            p = {
                'text': {'name': portfolio_detail['name']},
                'children': self.get_portfolio(portfolio_detail['children'])
                }
            children.append(p)
        return children
