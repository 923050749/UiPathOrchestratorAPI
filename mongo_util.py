try:
    import pymongo
    import json
    import os
    from enum import Enum
except Exception as e:
    raise Exception("Module Missing :{}".format(e))

class Singleton(type):

    """ Singleton Design Pattern  """

    _instance = {}

    def __call__(cls, *args, **kwargs):

        """ if instance already exist dont create one  """

        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

class MongoDbSettings(object):
    def __init__(self,
                 connection_string,
                 database_name,
                 collection_name):
        self.connection_string = connection_string
        self.collection_name = collection_name
        self.database_name = database_name


class MongoDB(metaclass=Singleton):

    def __init__(self, mongo_db_settings):
        self.mongo_db_settings = mongo_db_settings
        if type(self.mongo_db_settings).__name__ != "MongoDbSettings":
            raise Exception("Please mongo_db_settings  pass correct Instance")

        self.client = pymongo.MongoClient(self.mongo_db_settings.connection_string)
        self.cursor = self.client[self.mongo_db_settings.database_name][
            self.mongo_db_settings.collection_name
        ]

    def get_data(self, query={}, mongo_batch_size=100):

        # 2000
        total_count = self.cursor.count_documents(filter=query)

        # 2000//100
        total_pages = total_count // mongo_batch_size

        page_size = mongo_batch_size

        if total_count % mongo_batch_size != 0:
            total_pages += 1

        for page_number in range(1, total_pages + 1):

            skips = page_size * (page_number - 1)
            cursor = self.cursor.find(query).skip(skips).limit(page_size)
            yield [x for x in cursor]


class Connector(Enum):
    MONGODB_QA = MongoDB(
        mongo_db_settings=MongoDbSettings(
            connection_string="",
            database_name="",
            collection_name="",
        )
    )

def main():

    """instance"""
    connector  = Connector.MONGODB_QA.value

    query = {}
    mongo_data = connector.get_data(query=query)

    while True:
        try:
            data = next(mongo_data)
        except StopIteration:
            break
        except Exception as e:
            continue

