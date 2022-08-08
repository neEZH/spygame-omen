from peewee import *
from playhouse.postgres_ext import *

class BaseModel(Model):
    class Meta:
        database = conn


class User(BaseModel):
    # id = AutoField(column_name='ID', primary_key=True)
    tg_id = IntegerField(column_name='tgid', primary_key=True)
    nickname = CharField(column_name='tg_nickname', null=True)

    class Meta:
        table_name = 'users'


class Rooms(BaseModel):
    id = AutoField(column_name='ID', primary_key=True)
    code = TextField(column_name='code')
    players = ArrayField(IntegerField, column_name='players')
    selection = JSONField(column_name='selection')
    spy = IntegerField(column_name='spy_tgid', null=True)
    owner = IntegerField(column_name='owner')

    class Meta:
        table_name = 'rooms'


class Places(BaseModel):
    id = AutoField(column_name='ID', primary_key=True)
    name = CharField(column_name='place_name')
    owner = IntegerField(column_name='owner')

    class Meta:
        table_name = 'places'
