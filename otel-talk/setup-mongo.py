import pymongo
import config1

cfg= config1.Config

with pymongo.MongoClient(f"mongodb://{cfg.CATALOG['MONGO_HOST']}:{int(cfg.CATALOG['MONGO_PORT'])}") as mgclient:
    mgdb = mgclient[ cfg.CATALOG['MONGO_DB'] ]
    mgcol = mgdb[ cfg.CATALOG['MONGO_COL'] ]

    catalog_data = [
          { '_id': 11, 'name': 'xiomi 15', 'price': 20000 },
          { '_id': 10, 'name': 'MacBook Pro 13', 'price': 250000 }
        ]
    ins = mgcol.insert_many(catalog_data),{ upsert: true }


with pymongo.MongoClient(f"mongodb://{cfg.WAREHOUSE['MONGO_HOST']}:{int(cfg.WAREHOUSE['MONGO_PORT'])}") as mgclient:
    mgdb = mgclient[ cfg.WAREHOUSE['MONGO_DB'] ]
    mgcol = mgdb[ cfg.WAREHOUSE['MONGO_COL'] ]

    warehouse_data = [
              { _id: 'safeer', pin: 560066, city: 'Bangalore' },
              { _id: 'jondoe', pin: 560077, city: 'Bangalore' },
              { _id: 'janedoe', pin: 560088, city: 'Bangalore' }
        ]
    ins = mgcol.insert_many(warehouse_data, { upsert: true })


