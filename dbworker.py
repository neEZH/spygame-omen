from peewee import *
from dbModel import *
import os

# from psycopg2 import *

pg_db = PostgresqlDatabase(os.environ['DATABASE_URL'])


def user_start(user_id, username):
    user = User.get_or_create(tg_id=user_id)
    user.nickname = username
    user.save()


def create_room(user_id, code, select_method):
    room = Rooms(room_code=code,
                 selection=select_method,
                 players=[user_id],
                 owner=user_id)
    room.save()


def join_room(user_id, room_code):
    room = Rooms.get_or_none(Rooms.code == room_code)
    if room is not None:
        room.players.append(user_id)
        room.save()
        return room
    else:
        return None


def add_place(place_name, user_id):
    new_place = Places(name=place_name,
                       owner=user_id)
    new_place.save()


def get_places_by_id(place_id):
    place = Places.get_or_none(Places.id == place_id)
    return place.name


def get_places_by_owner(user_ids):
    # find places where Places.owner in user_ids[]
    query = Places.select().where(Places.owner << user_ids)
    places_selected = query.dicts().execute()
    return places_selected


def set_spy(room_code, user_id):
    query = Rooms.update(spy=user_id).where(Rooms.code == room_code)
    query.execute()
