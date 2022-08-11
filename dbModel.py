from playhouse.postgres_ext import *
import os


pg_db = PostgresqlDatabase(os.environ['DATABASE_URL'])


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
    code = TextField(column_name='code', primary_key=True)
    players = ArrayField(IntegerField, column_name='players')
    selection = SmallIntegerField(column_name='selection', default=0)
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


def create_tables():
    with pg_db:
        pg_db.create_tables([User, Rooms, Places])
