#Author     : Abhishek Kumar Dwivedi
#Created On : 19/6/2020

from flask import Flask, request, jsonify 
from flask_restful import Api, Resource
import os
import pandas as pd
from random import randint
#Initilizing app parameters
app = Flask(__name__)

# Getting your base path of file
baseDir = os.path.abspath(os.path.dirname(__file__))
cartDBpath = os.path.join(baseDir, 'cartdata.xlsx')
print(baseDir)

#check if file is present or not  if not then create a new file(database)
if not os.path.exists(cartDBpath):
    df = pd.DataFrame(columns=['Id', 'Name', 'Description', 'Price', 'Quantity'])
    df.to_excel('cartdata.xlsx', index=False)

#get whole cart data
@app.route("/cart", methods=['GET'])
def get():
    if os.path.exists(cartDBpath):
        df = pd.read_excel("cartdata.xlsx")
        data = df.to_json(orient="records")
        return data

# get single cart data by providing id
@app.route("/cart/<int:id>", methods=['GET'])
def getid(id):
    if os.path.exists(cartDBpath):
        df = pd.read_excel("cartdata.xlsx")
        i=0
        for rowId in df.Id:
            if id == rowId:
                return df.iloc[i].to_json(orient="records")
            i += 1

        return "item not found in cart"


# Update single Item data by providing id
@app.route("/cart/<int:id>", methods=['PUT'])
def put(id):
    if os.path.exists(cartDBpath):
        df = pd.read_excel("cartdata.xlsx")
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']
        i = 0
        for rowId in df.Id:
            if id == rowId:
                df.loc[i,['Name', 'Description', 'Price', 'Quantity']] = [name, description, price, qty]
                df.to_excel('cartdata.xlsx', index=False)
                return str(id) + " Updated"
            i +=1

        return "item not found in cart"

#Post item in cart
@app.route("/cart", methods=['POST'])
def post():
    if os.path.exists(cartDBpath):
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']
        idfy = randint(1, 9999)
        df = pd.read_excel("cartdata.xlsx")
        print(df)
        df1 = pd.DataFrame({'Id': [idfy], 'Name': [name], 'Description': [description], 'Price': [price], 'Quantity': [qty]}, index=None)
        df = pd.concat([df, df1], axis=0, ignore_index=False)
        df.to_excel('cartdata.xlsx', index=False)
        return 'Item Added'
    else:
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']
        idfy = randint(1, 9999)
        ret = df = pd.DataFrame({'Id': [idfy], 'Name': [name], 'Description': [description], 'Price': [price], 'Quantity': [qty]}, index=None)
        df.to_excel('cartdata.xlsx', index=False)
        return 'Item Added'

# delete single cart Item by providing id
@app.route("/cart/<int:id>", methods=['DELETE'])
def delete(id):
    if os.path.exists(cartDBpath):
        df = pd.read_excel("cartdata.xlsx")
        for rowId in df.Id:
            if id == rowId:
                df = df.set_index("Id")
                modifiedDf = df.drop(rowId, axis=0)
                modifiedDf.to_excel('cartdata.xlsx', index=True)
                return str(rowId) + ' deleted'

        return "item not found in cart"


#Run Server
if __name__ =='__main__':
    app.run(debug=True)