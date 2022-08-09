import random
import string
import dbworker as db
import json

msg_file = open('local.json')
message = json.load(msg_file)
msg_file.close()


def generate_room_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))


def new_player(u_id, user_name, is_bot):
    if not is_bot:
        db.user_start(user_id=u_id, username=user_name)
        return message["en"]["messages"]["new player"].format(user_name)


def new_room(u_id):
    room_code = generate_room_code()
    db.create_room(u_id, room_code)
    return message["en"]["messages"]["room created"].format(room_code)


def join_room(u_id, room_code):
    room = db.join_room(u_id, room_code)
    if room:
        return message["en"]["messages"]["join done"].format("\n".join(room.players))
    else:
        return message["en"]["messages"]["join failed"]


def play_game(user_id):
    room = db.get_room_by_owner(user_id)
    place = select_place(room)
    spy = select_spy(room.players)
    game_setup = {}
    for player in room.players:
        if player == spy:
            game_setup[player] = message["en"]["messages"]["spy"]
        else:
            game_setup[player] = message["en"]["messages"]["place"].format(str(place))
    return game_setup


def select_spy(players):
    spy_id = random.randint(0, len(players))
    return players[spy_id]


def select_place(game_room):
    # selections
    # 0 - owner only added
    # 1 - players added
    # 2 - all places
    if game_room.selection == 0:
        places_arr = db.get_places_by_owner(game_room.owner)
    elif game_room.selection == 1:
        places_arr = db.get_places_by_owner(game_room.players)
    elif game_room.selection == 2:
        places_arr = db.get_places_all()
    place = places_arr[random.randint(0, len(places_arr))]
    return place


def add_place(user_id, place_name):
    places_arr = db.add_place(place_name, user_id)
    return message["en"]["messages"]["added place"].format(place_name, "\n".join(places_arr))
