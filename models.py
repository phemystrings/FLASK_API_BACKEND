import json
from uuid import uuid4


def get_all():
    with open('db.json', 'r') as file:
        reader = file.read()
        return json.loads(reader)


def save(updatedDB):
    with open('db.json', 'w') as newFile:
        newFile.write(json.dumps(updatedDB))
        newFile.close()


def get_one(id):
    for item in get_all():
        if item['id'] == id:
            return item


def create_new(formData):
    formData['id'] = uuid4().hex
    DB = get_all()
    DB.append(formData)
    save(DB)


def update_Data(id, formData):
    DB = get_all()
    DB[DB.index(get_one(id))].update(formData)
    save(DB)
    return {'data': 'Data Updated'}


def delete_Data(id):
    DB = get_all()
    del DB[DB.index(get_one(id))]
    save(DB)
    return {'data': 'Data Deleted Successfully!'}
