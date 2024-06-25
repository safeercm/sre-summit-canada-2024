from flask import Flask, request, jsonify
from time import sleep
import requests
import config

import mysql.connector as connector

app = Flask(__name__)

@app.route("/productpage" , methods=['GET'])
def genProductPage():
    args = request.args
    productid=int(args.get('id'))
    username=args.get('user')
    app.config.from_object(config.Config)
    cfg=app.config
    print(cfg)
    r_prod_details = requests.get(url=cfg['CATALOG']['URI'], params=[('id',productid)] )
    if r_prod_details.status_code != 200:
        return "Product Unavailable", 400
    page={}
    prod_details = r_prod_details.json()
    page['product']=prod_details
    print(prod_details)
    
    r_address = requests.get(url=cfg['ADDRESSBOOK']['URI'],params=[('user', username)])
    if r_address.status_code != 200:
        return 'No such user/User has no address', 400
    address = r_address.json()
    pincode = address['pin']
    page['address']=address

    r_serviceable = requests.get(url=cfg['SERVICEABLE']['URI'],params=[('pin',pincode),('id',productid)])
    if r_serviceable.status_code != 200:
        return 'Serviceability info unavailable', 400
    print(r_serviceable.text)
    page['serviceable']=r_serviceable.json()

    return jsonify(page)
