from flask import Flask, request, jsonify
from time import sleep

import pymongo
import config

app = Flask(__name__)


@app.route("/catalog" , methods=['GET'])
def getProdcut():
    args = request.args
    productid=int(args.get('id'))
    app.config.from_object(config.Config)
    cfg=app.config
    myclient = pymongo.MongoClient(f"mongodb://{cfg['CATALOG']['MONGO_HOST']}:{int(cfg['CATALOG']['MONGO_PORT'])}")
    mydb = myclient[ cfg['CATALOG']['MONGO_DB'] ]
    mycol = mydb[ cfg['CATALOG']['MONGO_COL'] ]
    product = mycol.find_one({'_id':int(productid)})
    return jsonify(product)
    


