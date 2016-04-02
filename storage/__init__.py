from pymongo import MongoClient
import gridfs, json, os

with open(os.path.join(os.path.dirname(__file__), 'config.json')) as config_file:
    config = json.load(config_file)

host = config['storage-config']['host']
port = config['storage-config']['port']
db = MongoClient(host, port).images
gfs = gridfs.GridFS(db)

from storage import filestorage
