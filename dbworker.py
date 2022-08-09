from peewee import *
from dbModel import *
import os

# from psycopg2 import *

pg_db = PostgresqlDatabase(os.environ['DATABASE_URL'])


def user_start(user_id, username):
    user = User.get_or_create(tg_id=user_id)
    user.nickname = username
    user.save()


def create_room(user_id, code, select_method=0):
    room = Rooms.get_or_create(owner=user_id)
    room.room_code = code
    room.selection = select_method
    room.players = [user_id]
    room.owner = user_id
    room.save()


def join_room(user_id, room_code):
    room = Rooms.get_or_none(Rooms.code == room_code)
    if room is not None:
        room.players.append(user_id)
        room.save()
    return room


def get_room_by_owner(user_id):
    room = Rooms.get_or_none(Rooms.owner == user_id)
    return room


def add_place(place_name, user_id):
    new_place = Places(name=place_name,
                       owner=user_id)
    new_place.save()
    return Places.select().where(Places.owner == user_id)


def get_places_by_id(place_id):
    place = Places.get_or_none(Places.id == place_id)
    return place.name


def get_places_all():
    query = Places.select()
    return query.dicts().execute()


def get_places_by_owner(user_ids):
    # find places where Places.owner in user_ids[]
    query = Places.select().where(Places.owner << user_ids)
    return query #.dicts().execute()


def set_spy(room_code, user_id):
    query = Rooms.update(spy=user_id).where(Rooms.code == room_code)
    query.execute()
