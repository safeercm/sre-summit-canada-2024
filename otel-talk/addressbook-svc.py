from flask import Flask, request, jsonify
from time import sleep

import pymongo
import config

app = Flask(__name__)


@app.route("/address" , methods=['GET'])
def showProdcut():
    args = request.args
    userid=args.get('user')
    app.config.from_object(config.Config)
    cfg=app.config
    myclient = pymongo.MongoClient(f"mongodb://{cfg['ADDRESSBOOK']['MONGO_HOST']}:{int(cfg['ADDRESSBOOK']['MONGO_PORT'])}")
    mydb = myclient[ cfg['ADDRESSBOOK']['MONGO_DB'] ]
    mycol = mydb[ cfg['ADDRESSBOOK']['MONGO_COL'] ]

    address = mycol.find_one({'_id': userid })
    print(address)
    return jsonify(address)
    
