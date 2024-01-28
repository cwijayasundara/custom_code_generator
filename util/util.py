import pandas as pd
import os


def safe_write(path, code):
    path = "./software/" + path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w+') as f:
        f.write(code)


df = pd.read_csv("rules/expanded_trade_attributes.csv")


def trade_attributes():
    return df["Trade Attribute"].tolist()


def trade_attribute_validations():
    return df["Attribute Validations"].tolist()


def trade_business_rules():
    return df["Business Rules"].tolist()
