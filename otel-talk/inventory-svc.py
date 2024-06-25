from flask import Flask, request, jsonify
from time import sleep

import mysql.connector as connector
import config

app = Flask(__name__)


@app.route("/inventory" , methods=['GET'])
def getInventory():
        args = request.args
        productid=int(args.get('id'))
        app.config.from_object(config.Config)
        cfg=app.config
        connection = connector.connect(host=cfg['INVENTORY']['MYSQL_HOST'],user=cfg['INVENTORY']['MYSQL_USER'], password=cfg['INVENTORY']['MYSQL_PASS'], database=cfg['INVENTORY']['MYSQL_DB'])
        cursor = connection.cursor()
        query = f"select wh_id from {cfg['INVENTORY']['MYSQL_TABLE']} where product_id={productid}"
        cursor.execute(query)
        result = cursor.fetchall()
        warehouse_list={'wh':[]}
        for r in result:
            warehouse_list['wh'].append(r[0])
        return jsonify(warehouse_list)


