from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".credentials"))

class Config():
    PRODUCTPAGE = {
            "URI": "http://productpage.api.sre:5000/productpage",
            }
    CATALOG = {
            "URI": "http://catalog.api.sre:5001/catalog",
            "MONGO_HOST": "catalog.mongo.sre",
            "MONGO_PORT": 27017,
            "MONGO_DB": "catalog",
            "MONGO_COL": "products"
            }
    ADDRESSBOOK = {
            "URI": "http://addressbook.api.sre:5002/address",
            "MONGO_HOST": "addressbook.mongo.sre",
            "MONGO_PORT": 27017,
            "MONGO_DB": "addressbook",
            "MONGO_COL": "addresses"
            }
    SERVICEABLE = {
            "URI": "http://serviceable.api.sre:5003/serviceable",
            }
    WAREHOUSE = {
            "URI": "http://warehouse.api.sre:5005/warehouse",
            "MYSQL_HOST":" warehouse.mysql.sre",
            "MYSQL_PORT": 3306,
            "MYSQL_USER": environ.get('WAREHOUSE_MY_USER'),
            "MYSQL_PASS": environ.get('WAREHOUSE_MY_PASS'),
            "MYSQL_DB": "warehouse",
            "MYSQL_TABLE": "warehouses"
            }
    INVENTORY = {
            "URI": "http://inventory.api.sre:5004/inventory",
            "MYSQL_HOST": "inventory.mysql.sre",
            "MYSQL_PORT": 3306,
            "MYSQL_USER": environ.get('INVENTORY_MY_USER'),
            "MYSQL_PASS": environ.get('INVENTORY_MY_PASS'),
            "MYSQL_DB": "inventory",
            "MYSQL_TABLE": "inventories"
            }

