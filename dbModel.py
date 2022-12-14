from playhouse.postgres_ext import *
from playhouse.db_url import connect
import os


pg_db = connect(os.environ['DATABASE_URL'])


class BaseModel(Model):
    class Meta:
        database = pg_db


class User(BaseModel):
    # id = AutoField(column_name='ID', primary_key=True)
    tg_id = IntegerField(column_name='tgid', primary_key=True)
    nickname = CharField(column_name='tg_nickname', null=True)
    # local = CharField(column_name="language", default="en")

    class Meta:
        table_name = 'users'


class Rooms(BaseModel):
    # id = AutoField(column_name='ID', primary_key=True)
    code = TextField(column_name='code', null=True)
    players = ArrayField(IntegerField, column_name='players', null=True)
    selection = SmallIntegerField(column_name='selection', default=0)
    spy = IntegerField(column_name='spy_tgid', null=True)
    owner = IntegerField(column_name='owner', primary_key=True)

    class Meta:
        table_name = 'rooms'


class Places(BaseModel):
    id = AutoField(column_name='ID', primary_key=True)
    name = CharField(column_name='place_name')
    owner = IntegerField(column_name='owner')

    class Meta:
        table_name = 'places'


def create_tables():
    try:
        pg_db.connect()
        pg_db.create_tables([User, Rooms, Places])
        print(pg_db.get_tables())
    except Exception as e:
        print(e)
    pg_db.close()
