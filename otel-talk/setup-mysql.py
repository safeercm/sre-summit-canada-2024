import mysql.connector as connector
import config1

cfg=config1.Config()

connection = connector.connect(host=cfg.INVENTORY['MYSQL_HOST'],user=cfg.INVENTORY['MYSQL_USER'], password=cfg.INVENTORY['MYSQL_PASS'])
query=f"create database if not exists {cfg.INVENTORY['MYSQL_DB']}"
cursor = connection.cursor()
cursor.execute(query)
cursor.reset()
connection.database = cfg.INVENTORY['MYSQL_DB']

query = f" create table if not exists `{cfg.INVENTORY['MYSQL_TABLE']}` (`product_id` int(11) NOT NULL, `wh_id` int(6) NOT NULL, PRIMARY KEY (`product_id`,`wh_id`));"
cursor.execute(query)
cursor.reset()

inventory_data = [[10,200],[11,200],[11,100] ]

query=f"insert ignore into `{cfg.INVENTORY['MYSQL_TABLE']}` value (%s,%s)"
cursor.executemany(query,inventory_data)
connection.commit()

connection.close()


connection = connector.connect(host=cfg.WAREHOUSE['MYSQL_HOST'],user=cfg.WAREHOUSE['MYSQL_USER'], password=cfg.WAREHOUSE['MYSQL_PASS'])
query=f"create database if not exists {cfg.WAREHOUSE['MYSQL_DB']}"
cursor = connection.cursor()
cursor.execute(query)
cursor.reset()
connection.database = cfg.WAREHOUSE['MYSQL_DB']

query = f" create table if not exists `{cfg.WAREHOUSE['MYSQL_TABLE']}` (`wh_id` int(6) NOT NULL, `svc_pin` int(8) NOT NULL, `address` varchar(255), PRIMARY KEY (`wh_id`,`svc_pin`));"
cursor.execute(query)
cursor.reset()

inventory_data = [
[100,560066,'Whitefield, BLR, IN'],
[100,560067,'Whitefield, BLR, IN'],
[100,560068,'Whitefield, BLR, IN'],
[200,560066,'HAL, BLR, IN'],
[200,560071,'HAL, BLR, IN'],
[200,560072,'HAL, BLR, IN'],
[200,560073,'HAL, BLR, IN']
        ]

query=f"insert ignore into `{cfg.WAREHOUSE['MYSQL_TABLE']}` value (%s,%s,%s)"
cursor.executemany(query,inventory_data)
connection.commit()

connection.close()


