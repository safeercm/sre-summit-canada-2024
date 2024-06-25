from flask import Flask, request, jsonify
from time import sleep
import requests
import config

import mysql.connector as connector

app = Flask(__name__)

@app.route("/serviceable" , methods=['GET'])
def isServiceable():
    args = request.args
    productid=int(args.get('id'))
    pincode=int(args.get('pin'))
    app.config.from_object(config.Config)
    cfg=app.config

    r_wh_for_pin = requests.get(url=cfg['WAREHOUSE']['URI'],params=[('pin',pincode)])
    wh_for_pin = r_wh_for_pin.json()
    r_wh_for_id = requests.get(url=cfg['INVENTORY']['URI'],params=[('id',productid)])
    wh_for_id = r_wh_for_id.json()
    if len(wh_for_pin['wh']) == 0 or len(wh_for_id['wh']) == 0:
        return(jsonify({'serviceable':'no'}))
    else:
        for wh_pin in wh_for_pin['wh']:
            for wh_id in wh_for_id['wh']:
                if wh_pin == wh_id:
                    return(jsonify({'serviceable':'yes'}))
        return(jsonify({'serviceable':'no'}))
