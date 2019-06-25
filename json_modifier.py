import os
import json

from settings import PORTFOLIO_DIRECTORY


def get_all_portfolio_jsons():
    portfolio_files = []

    for filename in os.listdir(PORTFOLIO_DIRECTORY):
        if filename.endswith(".json"):
            portfolio_files.append(os.path.join(PORTFOLIO_DIRECTORY, filename))

    return portfolio_files


def get_json_title(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
        return data["name"]


def get_list_portfolio_id_name():
    portfolio_files = get_all_portfolio_jsons()
    portfolios = {}
    for i, name in enumerate(portfolio_files):
        portfolios["portfolio_" + str(i)] = name
    return portfolios


class PortfolioTreeMapper:

    def get_json(self, json_path):
        with open(json_path) as json_file:
            data = json.load(json_file)
            children = self.get_portfolio(data['children'])
            if children:
                name = data['name']
            else:
                name = "No subportfolios in portfolio {}".format(data['name'])
            return {
                'text': {'name': name},
                'children': children
            }

    def get_portfolio(self, portfolio_children):
        children = []
        for portfolio_detail in portfolio_children:
            p = {
                'text': {'name': portfolio_detail['name']},
                'children': self.get_portfolio(portfolio_detail['children'])
                }
            children.append(p)
        return children
