from glob import glob
import json
import os


def load(folder):
    db = {}
    jsonfiles = glob(folder+'/*.json')
    for f in jsonfiles:
        key = os.path.basename(f).rsplit('.', 1)[0]
        with open(f, 'r') as fobj:
            db[key] = json.load(fobj)
    return db

def save(db, folder):
    if not type(db) == dict:
        raise Exception('JSON database must be a dict')
    jsonfiles = glob(folder+'/*.json')
    for key in db:
        filename = '{0}/{1}.json'.format(folder, key)
        if not filename in jsonfiles:
            with open(filename, 'w') as f:
                json.dump(db[key], f)
