def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    hello_message = []
    for name in names:
        hello_message.append(f"Hello, my name is {name}.")
    return hello_message

def assign_rooms(names):
    room_assignments = []
    room_num = 1
    for name in names:
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {room_num}!")
        room_num += 1
    return room_assignments

def printer(names):
    room_num = 1
    for name in names:
        print(f"Hello, my name is {name}.")
    for name in names:
        print(f"Hello, {name}! You'll be assigned to room {room_num}!")
        room_num += 1
