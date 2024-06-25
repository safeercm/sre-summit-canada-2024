from flask import Flask, request, jsonify
from time import sleep

import mysql.connector as connector
import config


app = Flask(__name__)


@app.route("/warehouse" , methods=['GET'])
def getWarehouses():
        args = request.args
        pincode=int(args.get('pin'))
        app.config.from_object(config.Config)
        cfg=app.config
        connection = connector.connect(host=cfg['WAREHOUSE']['MYSQL_HOST'],user=cfg['WAREHOUSE']['MYSQL_USER'], password=cfg['WAREHOUSE']['MYSQL_PASS'], database=cfg['WAREHOUSE']['MYSQL_DB'])
        cursor = connection.cursor()
        query = f"select wh_id from {cfg['WAREHOUSE']['MYSQL_TABLE']} where svc_pin={pincode}"
        cursor.execute(query)
        result = cursor.fetchall()
        warehouse_list={'wh':[]}
        for r in result:
            warehouse_list['wh'].append(r[0])
        return jsonify(warehouse_list)


