from pymongo import MongoClient

client = MongoClient("mongodb://localhost")
db = client['test']


def task1_part1():
    cursor = db.restaurants.find({'cuisine': 'Indian'})
    for i in cursor:
        print(i['name'])


def task1_part2():
    cursor = db.restaurants.find({'$or': [{'cuisine': 'Indian'}, {'cuisine': 'Thai'}]})
    for i in cursor:
        print(i['name'])


def task1_part3():
    cursor = db.restaurants.find(
        {'address.building': '1115', 'address.street': 'Rogers Avenue', 'address.zipcode': '11226'})
    for i in cursor:
        address = i['name']
        print(address)


def task2():
    db.restaurants.insert_one({'borough': 'Manhattan', 'cuisine': 'Italian', 'name': 'Vella',
                               'restaurant_id': '41704620', 'address':
                                   {'building': '1480', 'coord': [-73.9557413, 40.7720266], 'zipcode': '10075',
                                    'street': '2 Avenue'},
                               'grades': [{'date': '2014-10-01T00:00:00.000Z', 'grade': 'A', 'score': 11}]})


def task3_part1():
    db.restaurants.delete_one({'borough': 'Manhattan'})


def task3_part2():
    db.restaurants.delete_many({'cuisine': 'Thai'})


def task4():
    cursor = db.restaurants.find({'address.street': 'Rogers Avenue'})

    for i in cursor:
        if i['grades'].count({'grade': 'A'}) > 1:
            db.restaurants.delete_one({'_id': i['_id']})
        else:
            db.restaurants.update_one(
                {'_id': i['_id']},
                {'$push': {'grades': {'data': '2022-04-25T00:00:00.000Z', 'grade': 'C', 'score': '3'}}}
            )
