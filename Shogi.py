import turtle
import math
# Figure out if we should do a bunch of spacing or not
# Too much spacing = disconnected code
# Too little spacing = too clustered + bad grade = not good


def make_yards():
    make = turtle.Turtle()
    make.ht()
    make.speed(0)
    make.penup()
    make.setpos(-400, -175)
    make.pendown()
    make.forward(150)
    make.back(150)
    make.left(180)
    for q in range(2):
        if q == 1:
            make.penup()
            make.setpos(400, 175)
            make.pendown()
            make.left(90)
            make.forward(150)
            make.back(150)
            make.right(180)
        for i in range(7):
            if i % 2 == 0:
                make.right(90)
                make.forward(50)
                make.right(90)
                make.forward(150)
            else:
                make.left(90)
                make.forward(50)
                make.left(90)
                make.forward(150)
        make.right(90)
        make.forward(350)
        make.right(90)
        make.forward(50)
        make.right(90)
        make.forward(350)
        make.left(90)
        make.forward(50)
        make.left(90)
        make.forward(350)
        make.right(90)
        make.forward(50)
        make.right(90)
        make.forward(350)


def round_to_mid(x, y):
    for location in middle:
        if location[0] - 25 <= x <= location[0] + 25 and location[1] - 25 <= y <= location[1] + 25:
            return [location[0], location[1]]
    return ["na", "na"]


def mid():
    midd = []
    for midd_y in range(9):
        for midd_x in range(9):
            midd.append([-200 + midd_x * 50, 200 - midd_y * 50])
    return midd


def legal_move(piece, turn_counted):
    global temp_move_list
    restrict = 0
    inactive_player = 0
    active_player_list = []
    inactive_player_list = []
    if turn_counted % 2 != 0:
        active_player_list = player_one
        inactive_player_list = player_two
        if piece in player_one:
            inactive_player = 2
            restrict = 1
    elif turn_counted % 2 == 0:
        active_player_list = player_two
        inactive_player_list = player_one
        if piece in player_two:
            inactive_player = 1
            restrict = 1
    if restrict == 1:
        piece_name = piece[0]
        for rule in movement_rules:
            if piece_name == rule[0]:
                move_list = rule[1:len(rule)]
                for location in move_list:
                    fail = 0
                    hit = 0
                    color = "blue"
                    for add in range(int(len(location) / 2)):
                        if fail == 0 and [(-1) ** inactive_player * location[0 + 2 * add] + piece[1],
                                          (-1) ** inactive_player * location[1 + 2 * add] + piece[2]] in middle:
                            for part in active_player_list:
                                if (-1) ** inactive_player * location[0 + 2 * add] + piece[1] == part[1] and (
                                        -1) ** inactive_player * location[1 + 2 * add] + piece[2] == part[2]:
                                    fail = 1
                            for part_2 in inactive_player_list:
                                if (-1) ** inactive_player * location[0 + 2 * add] + piece[1] == part_2[1] and (
                                        -1) ** inactive_player * location[1 + 2 * add] + piece[2] == part_2[2]:
                                    hit = 1
                            if fail == 0:
                                if hit == 1:
                                    color = "red"
                                    fail = 1
                                highlight_space((-1) ** inactive_player * location[0 + 2 * add] + piece[1],
                                                (-1) ** inactive_player * location[1 + 2 * add] + piece[2], color)
                                temp_move_list.append([(-1) ** inactive_player * location[0 + 2 * add] + piece[1],
                                                       (-1) ** inactive_player * location[1 + 2 * add] + piece[2]])
    else:
        temp_move_list = middle[:]


# This function highlights a square of your choice to display valid moves.
# It can be used to highlight enemy squares red, or allied squares blue.
def highlight_space(x, y, color):

    highlighter.color(color)
    highlighter.pensize(2)
    highlighter.penup()

    # x+25 and y-25 moves highlighting turtle from the centre to the bottom right corner of the highlighted square.
    # This saves us the trouble of having to give orders to the turtle to orient it to a spot where it can draw a square
    # When we start it off at a corner, we just have to give it orders to draw a simple square.
    highlighter.setpos(x + 25, y - 25)
    highlighter.pendown()

    # This is a basic square drawing loop
    for i in range(4):
        highlighter.left(90)
        highlighter.forward(50)


def promote(piece):
    if piece[0] in promotion:
        prompt = wn.textinput("Promotion", "Promote?(Yes or No)")
        if prompt.upper() == "YES":
            name = piece[0]
            new_name = "promoted\n" + name
            del piece[0]
            piece.insert(0, new_name)
            return piece
    else:
        return piece


def make_board():
    maker = turtle.Turtle()
    maker.ht()
    maker.speed(0)
    maker.penup()
    maker.setpos(225, -225)
    maker.pendown()
    for lines in range(2):
        maker.left(90)
        for repeat in range(5):
            maker.forward(450)
            maker.left(90)
            maker.forward(50)
            maker.left(90)
            maker.forward(450)
            if repeat != 4:
                maker.right(90)
                maker.forward(50)
                maker.right(90)


def death(piece, turn_counted):
    inactive_player_list = []
    inactive_player_dead = []
    active_player = 0
    x = 0
    y = 0
    done = 0
    if turn_counted % 2 != 0:
        inactive_player_list = player_two
        inactive_player_dead = player_two_dead
        active_player = 1
    elif turn_counted % 2 == 0:
        inactive_player_list = player_one
        inactive_player_dead = player_one_dead
        active_player = 2
    inactive_player_list.remove(piece)
    turtle_name = piece[3]
    turtle_name.clear()
    for test_spot in range(21):
        if done != 1:
            (row_spot, value) = math.modf(test_spot / 3)
            fail = 0
            for dead in inactive_player_dead:
                if dead[1] == (-1) ** active_player * (375 - 150 * row_spot) and dead[2] == 150 - 50 * math.floor(
                        test_spot / 3):
                    fail = 1
            if fail != 1:
                x = (-1) ** active_player * (375 - 150 * row_spot)
                y = 150 - 50 * math.floor(test_spot / 3)
                done = 1
    turtle_name.setpos(x, y)
    turtle_name.right(180)
    turtle_name.write(piece[0] + "\n", align="center", font=("Arial", 7, "bold"))
    del piece[1]
    piece.insert(1, x)
    del piece[2]
    piece.insert(2, y)
    inactive_player_dead.append(piece)


def move(u, v):
    global turn_counter
    cord = round_to_mid(u, v)
    x = cord[0]
    y = cord[1]
    fail = 0
    returned = 0
    legal = 0
    active_player_list = []
    inactive_player_list = []
    inactive_player_dead = []
    selected = order_selected[len(order_selected) - 1]
    turtle_name = selected[3]
    start_x = 0

    if x == "na" and y == "na":
        fail = 1

    for test in temp_move_list:
        if test == cord:
            legal = 1
    if legal != 1:
        fail = 1

    if turn_counter % 2 != 0:
        active_player_list = player_one
        inactive_player_list = player_two
        inactive_player_dead = player_two_dead
        start_x = -200
    elif turn_counter % 2 == 0:
        active_player_list = player_two
        inactive_player_list = player_one
        inactive_player_dead = player_one_dead
        start_x = 200

    if fail != 1:

        if selected in inactive_player_dead:
            inactive_player_dead.remove(selected)
            active_player_list.append(selected)
            returned = 1

        for piece in active_player_list:
            if piece[1] == x and piece[2] == y:
                fail = 1

        for piece in inactive_player_list:
            if piece[1] == x and piece[2] == y:

                if returned == 1:
                    fail = 1

                else:
                    death(piece, turn_counter)

    if fail != 1:
        active_player_list.remove(selected)
        del selected[1]
        selected.insert(1, x)
        del selected[2]
        selected.insert(2, y)
        if x - start_x >= 300 and returned != 1:
            selected = promote(selected)
        active_player_list.append(selected)
        temp_move_list.clear()
        highlighter.clear()
        turtle_name.clear()
        turtle_name.setpos(x, y)
        turtle_name.color("black")
        turtle_name.write(selected[0] + "\n", align="center", font=("Arial", 7, "bold"))
        turn_counter += 1
        wn.onclick(select)

    else:
        temp_move_list.clear()
        highlighter.clear()
        turtle_name.color("black")
        wn.onclick(select)


def select(x, y):
    global turn_counter
    selected = []
    fail = 1
    active_player_list = []
    inactive_player_dead = []

    if turn_counter % 2 != 0:
        active_player_list = player_one
        inactive_player_dead = player_two_dead
    elif turn_counter % 2 == 0:
        active_player_list = player_two
        inactive_player_dead = player_one_dead

    for piece in active_player_list:

        if piece[1] - 25 <= x <= piece[1] + 25 and piece[2] - 25 <= y <= piece[2] + 25:
            selected = piece
            fail = 0

    for piece in inactive_player_dead:

        if piece[1] - 25 <= x <= piece[1] + 25 and piece[2] - 25 <= y <= piece[2] + 25:
            selected = piece
            fail = 0

    if fail != 1:
        turtle_ref = selected[3]
        turtle_ref.color("blue")
        order_selected.append(selected)
        legal_move(selected, turn_counter)
        wn.onclick(move)

    else:
        temp_move_list.clear()
        highlighter.clear()
        wn.onclick(select)


player_one = [['turtle1', 50, 100, turtle.Turtle()], ['turtle3', 100, 100, turtle.Turtle()]]
player_one_dead = []
player_two = [['turtle2', 200, 100, turtle.Turtle()], ['turtle4', 200, 150, turtle.Turtle()],
              ['turtle2', 200, 200, turtle.Turtle()], ['turtle2', 200, 50, turtle.Turtle()],
              ['turtle2', 200, 0, turtle.Turtle()]]

player_two_dead = []
movement_rules = [['turtle1', [0, 50], [0, -50], [50, 0, 100, 0, 150, 0]],
                  ['turtle2', [0, 50], [0, -50], [50, 0, 100, 0]],
                  ['turtle3', [0, 50], [0, -50]], ['turtle4', [0, 50], [0, -50]]]

temp_move_list = []
promotion = ['turtle1']
order_selected = []
middle = mid()
turn_counter = 1

wn = turtle.Screen()
wn.title("Shogi")
make_board()
make_yards()
wn.register_shape("tri", ((10, -3), (10, -20), (-10, -20), (-10, -3), (-5, 10), (5, 10)))
highlighter = turtle.Turtle()
highlighter.ht()
highlighter.speed(0)

for player_one_set in player_one:
    turtle_names = player_one_set[3]
    turtle_names.shape("tri")
    turtle_names.penup()
    turtle_names.setpos(player_one_set[1], player_one_set[2])
    turtle_names.write(player_one_set[0] + "\n", align="center", font=("Arial", 7, "bold"))

for player_two_set in player_two:
    turtle_names = player_two_set[3]
    turtle_names.shape("tri")
    turtle_names.penup()
    turtle_names.setpos(player_two_set[1], player_two_set[2])
    turtle_names.right(180)
    turtle_names.write(player_two_set[0] + "\n", align="center", font=("Arial", 7, "bold"))

if turn_counter == 1:
    wn.onclick(select)

wn.mainloop()