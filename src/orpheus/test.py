#!usr/bin/python3
# encoding: utf-8

# yus's test

import pandas as pd
from orpheus import Orpheus
from sklearn.tree import DecisionTreeClassifier

data_name = '../../data/WFH_WFO_dataset.csv'
target = 'Target'

df = pd.read_csv(data_name)
features = list(df.columns); features.remove(target)
X, y = pd.get_dummies(df[features]), df[target]

# usage for our class
orpheus_instance = Orpheus(
    data_name,
    DecisionTreeClassifier(random_state=0), # here should keep the return value of users
    X,
    y,
)
orpheus_instance.fit()
orpheus_instance.show_loss_curve()


### min's test
# orpheus_instance.save_metaData_toDB()
from orpheus import Orpheus
import sklearn_json as skljson
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from pymongo import MongoClient
from pymongo.database import Database
import click
import numpy as np

def dbtest():
    client = MongoClient(
        host='localhost',
        port=27017,
        # username=username,
        # password=password,
        # authSource=self.dbname,
        # authMechanism='SCRAM-SHA-256'
    )
    dbname = 'easyTest'
    db = Database(client, name=dbname)
    data_name = "easyData_v10"
    model_name = "dfc_v2"
    current_collection = db["metadata_collection"]
    # current_collection = db["data_collection"]

    filterQ = {"data_name": data_name, "model_name": model_name}
    projectionQ = {"_id": False, "meta_dict": {"evaluation_score": 1}}

    cursor = current_collection.find(filterQ, projectionQ)

    for i in cursor:
        print(i)

def orpheusTest():
    orpheus = Orpheus("easyTest", "tom", "123")
    data_name = "easyData"
    X = [[0, 0], [1, 1]]
    Y = [0, 1]
    model_name = "dfc_v2"
    model = DecisionTreeClassifier()

    # orpheus.view_all_data()
    #
    # orpheus.delete_data("all")
    # orpheus.view_all_data()
    orpheus.select_model_with_score_above(data_name, 0.1)
    # orpheus.save_Data_to_DB(data_name, X, Y)
    # orpheus.train(data_name, model_name, model)
    # orpheus.view_all_data()
    # orpheus.view_all_model("easyData")


# dbtest()

orpheusTest()
# click.secho(f'There exists {2} models with evaluation score > {2} for Data "{3}"')
# print('fo')
