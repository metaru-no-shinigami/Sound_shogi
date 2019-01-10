import turtle
import math
import time
import playsound



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


def flip():
    player_one_temp = player_one[:]
    player_two_temp = player_two[:]
    for piece_1 in player_one_temp:
        turtle_controller_1 = piece_1[3]
        x = -piece_1[1]
        y = -piece_1[2]
        wn.tracer(0,0)
        turtle_controller_1.setpos(x, y)
        turtle_controller_1.right(180)
        turtle_controller_1.clear()
        turtle_controller_1.write(piece_1[0] + "\n", align="center", font=("Arial", 7, "bold"))
        player_one.remove(piece_1)
        del piece_1[1]
        piece_1.insert(1, x)
        del piece_1[2]
        piece_1.insert(2, y)
        player_one.append(piece_1)

    for piece_2 in player_two_temp:
        turtle_controller = piece_2[3]
        x = -piece_2[1]
        y = -piece_2[2]
        wn.tracer(0, 0)
        turtle_controller.setpos(x, y)
        turtle_controller.right(180)
        turtle_controller.clear()
        turtle_controller.write(piece_2[0] + "\n", align="center", font=("Arial", 7, "bold"))
        player_two.remove(piece_2)
        del piece_2[1]
        piece_2.insert(1, x)
        del piece_2[2]
        piece_2.insert(2, y)
        player_two.append(piece_2)
    wn.tracer(1, 5)
    wn.update()


def legal_move(piece, turn_counted, highlight_bool):
    restrict = 0
    active_player_list = []
    inactive_player_list = []
    temp_move_list = []
    kill_zone = []
    if turn_counted % 2 != 0:
        active_player_list = player_one
        inactive_player_list = player_two
        if piece in player_one:
            restrict = 1
    elif turn_counted % 2 == 0:
        active_player_list = player_two
        inactive_player_list = player_one
        if piece in player_two:
            restrict = 1
    if restrict == 1:
        piece_name = piece[0]
        if piece_name == "King" and highlight_bool == 1:
            kill_zone = []
            for enemy_piece in inactive_player_list:
                kill_zone += legal_move(enemy_piece, turn_counted, 0)
        for rule in movement_rules:
            if piece_name == rule[0]:
                move_list = rule[1:len(rule)]
                for location in move_list:
                    fail = 0
                    hit = 0
                    color = "blue"
                    for cord in location:
                        (x, y) = cord
                        if fail == 0 and [x + piece[1], y + piece[2]] in middle:
                            for part in active_player_list:
                                if x + piece[1] == part[1] and y + piece[2] == part[2]:
                                    fail = 1
                            if piece[0] == "King" and highlight_bool == 1:
                                for dead_space in kill_zone:
                                    if (x + piece[1], y + piece[2]) == dead_space:
                                        fail = 1
                            for part_2 in inactive_player_list:
                                if x + piece[1] == part_2[1] and y + piece[2] == part_2[2]:
                                    hit = 1
                            if fail == 0:
                                if hit == 1:
                                    color = "red"
                                    fail = 1
                                if highlight_bool == 1:
                                    highlight_space(x + piece[1], y + piece[2], color)
                                temp_move_list.append([x + piece[1], y + piece[2]])
    else:
        temp_move_list = middle[:]
    return temp_move_list


def check_or_mate(turn_counted):
    active_player_list = []
    inactive_player_list = []
    kill_zone = []
    king = []
    check = 0
    if turn_counted % 2 != 0:
        active_player_list = player_one
        inactive_player_list = player_two
    elif turn_counted % 2 == 0:
        active_player_list = player_two
        inactive_player_list = player_one
    for king_finder in inactive_player_list:
        if king_finder[0] == "King":
            king = king_finder
    for enemy_piece in active_player_list:
        kill_zone += legal_move(enemy_piece, turn_counted, 0)
    king_danger.append(kill_zone)
    if (king[1], king[2]) in kill_zone:
        wn.textinput("Check", "Press Enter")
    if check == 1:
        king_movement = legal_move(king, turn_counted, 0)
        if king_movement == []:
            wn.textinput("Checkmate!", "You win!")
            return "end"


# This function highlights a square of your choice to display valid moves.
# It can be used to highlight enemy squares red, or allied squares blue.
def highlight_space(x, y, color):
    wn.tracer(0, 0)
    highlighter.color(color)
    highlighter.pensize(1)
    highlighter.penup()

    # x+25 and y-25 moves highlighting turtle from the centre to the bottom right corner of the highlighted square.
    # This saves us the trouble of having to give orders to the turtle to orient it to a spot where it can draw a square
    # When we start it off at a corner, we just have to give it orders to draw a simple square.
    highlighter.setpos(x + 24, y - 24)
    highlighter.pendown()

    # This is a basic square drawing loop
    for i in range(4):
        highlighter.left(90)
        highlighter.forward(48)
    wn.update()
    wn.tracer(1, 10)


def promote(piece):
    if piece[0] in promotion:
        prompt = wn.textinput("Promotion", "Promote?(Y or N)")
        while type(prompt) is None:
            prompt = wn.textinput("Promotion", "Promote?(Y or N)")
        if prompt.upper() == "Y":
            # playsound.playsound(path + '\Promotion.mp3')                            #Play promotion sound
            name = piece[0]
            new_name = "Pro " + name
            del piece[0]
            piece.insert(0, new_name)
            return piece
        elif prompt.upper() == "N":
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
    #playsound.playsound(path + '\Punch.mp3')                                          #Play punch sound
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
    name = piece[0]
    if name[0:4] == "Pro ":
        name = name[4:]
    turtle_name.write(name + "\n", align="center", font=("Arial", 7, "bold"))
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
    temp_move_list = selection_order_temp_move_list[len(selection_order_temp_move_list) -1]

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
    elif turn_counter % 2 == 0:
        active_player_list = player_two
        inactive_player_list = player_one
        inactive_player_dead = player_one_dead

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
        if y + 200 >= 300 and returned != 1:
            selected = promote(selected)
        active_player_list.append(selected)
        temp_move_list.clear()
        highlighter.clear()
        turtle_name.clear()
        # playsound.playsound(path + '\Move.mp3')                                             #play moving sound
        turtle_name.setpos(x, y)
        turtle_name.color("black")
        turtle_name.write(selected[0] + "\n", align="center", font=("Arial", 7, "bold"))
        check = check_or_mate(turn_counter)
        if check != "end":
            wn.textinput("Switching Phase", "Press Enter When Ready")
            flip()
            turn_counter += 1
            wn.onclick(select)

    else:
        highlighter.clear()
        turtle_name.color("black")
        wn.onclick(select)


def select(x, y):
    global turn_counter
    selected = []
    fail = 1
    active_player_list = []
    inactive_player_dead = []
    temp_move_list = []

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
        temp_move_list = legal_move(selected, turn_counter, 1)
        selection_order_temp_move_list.append(temp_move_list)
        wn.onclick(move)

    else:
        highlighter.clear()
        wn.onclick(select)


path = 'H:\Grade. 11\Computer Science\Final Project\Sounds'

player_one = [['Pawn', -200, -100, turtle.Turtle()], ['Pawn', -150, -100, turtle.Turtle()],
              ['Pawn', -100, -100, turtle.Turtle()], ['Pawn', -50, -100, turtle.Turtle()],
              ['Pawn', 0, -100, turtle.Turtle()], ['Pawn', 50, -100, turtle.Turtle()],
              ['Pawn', 100, -100, turtle.Turtle()], ['Pawn', 150, -100, turtle.Turtle()],
              ['Pawn', 200, -100, turtle.Turtle()], ["Bishop", -150, -150, turtle.Turtle()],
              ["Rook", 150, -150, turtle.Turtle()], ["Lance", -200, -200, turtle.Turtle()],
              ["Knight", -150, -200, turtle.Turtle()], ["Silver", -100, -200, turtle.Turtle()],
              ["Gold", -50, -200, turtle.Turtle()], ["King", 0, -200, turtle.Turtle()],
              ["Gold", 50, -200, turtle.Turtle()], ["Silver", 100, -200, turtle.Turtle()],
              ["Knight", 150, -200, turtle.Turtle()], ["Lance", 200, -200, turtle.Turtle()]]
player_one_dead = []
player_two = [['Pawn', -200, 100, turtle.Turtle()], ['Pawn', -150, 100, turtle.Turtle()],
              ['Pawn', -100, 100, turtle.Turtle()], ['Pawn', -50, 100, turtle.Turtle()],
              ['Pawn', 0, 100, turtle.Turtle()], ['Pawn', 50, 100, turtle.Turtle()],
              ['Pawn', 100, 100, turtle.Turtle()], ['Pawn', 150, 100, turtle.Turtle()],
              ['Pawn', 200, 100, turtle.Turtle()], ["Bishop", 150, 150, turtle.Turtle()],
              ["Rook", -150, 150, turtle.Turtle()], ["Lance", 200, 200, turtle.Turtle()],
              ["Knight", 150, 200, turtle.Turtle()], ["Silver", 100, 200, turtle.Turtle()],
              ["Gold", 50, 200, turtle.Turtle()], ["King", 0, 200, turtle.Turtle()],
              ["Gold", -50, 200, turtle.Turtle()], ["Silver", -100, 200, turtle.Turtle()],
              ["Knight", -150, 200, turtle.Turtle()], ["Lance", -200, 200, turtle.Turtle()]]

player_two_dead = []
movement_rules = [['Pawn', [(0, 50)]],
                  ['Bishop', [(50, 50), (100, 100), (150, 150), (200, 200), (250, 250), (300, 300),
                              (350, 350), (400, 400)],
                   [(-50, -50), (-100, -100), (-150, -150), (-200, -200), (-250, -250),
                    (-300, -300), (-350, -350), (-400, -400)],
                   [(-50, 50), (-100, 100), (-150, 150), (-200, 200), (-250, 250), (-300, 300),
                    (-350, 350), (-400, 400)],
                   [(50, -50), (100, -100), (150, -150), (200, -200), (250, -250), (300, -300),
                    (350, -350), (400, -400)]],
                  ['Rook', [(0, 50), (0, 100), (0, 150), (0, 200), (0, 250), (0, 300), (0, 350), (0, 400)],
                   [(50, 0), (100, 0), (150, 0), (200, 0), (250, 0), (300, 0), (350, 0), (400, 0)],
                   [(-50, 0), (-100, 0), (-150, 0), (-200, 0), (-250, 0), (-300, 0), (-350, 0), (-400, 0)],
                   [(0, -50), (0, -100), (0, -150), (0, -200), (0, -250), (0, -300), (0, -350), (0, -400)]],
                  ['Lance', [(0, 50), (0, 100), (0, 150), (0, 200), (0, 250), (0, 300), (0, 350), (0, 400)]],
                  ['Knight', [(50, 100)], [(-50, 100)]],
                  ['Silver', [(0, 50)], [(50, 50)], [(-50, 50)], [(-50, -50)], [(50, -50)]],
                  ['Gold', [(0, 50)], [(50, 50)], [(-50, 50)], [(50, 0)], [(-50, 0)], [(0, -50)]],
                  ['King', [(0, 50)], [(50, 50)], [(-50, 50)], [(50, 0)], [(-50, 0)], [(0, -50)], [(-50, -50)],
                   [(50, -50)]], ['Pro Pawn', [(0, 50)], [(50, 50)], [(-50, 50)], [(50, 0)], [(-50, 0)], [(0, -50)]],
                  ['Pro Knight', [(0, 50)], [(50, 50)], [(-50, 50)], [(50, 0)], [(-50, 0)], [(0, -50)]],
                  ['Pro Lance', [(0, 50)], [(50, 50)], [(-50, 50)], [(50, 0)], [(-50, 0)], [(0, -50)]],
                  ['Pro Bishop', [(50, 50), (100, 100), (150, 150), (200, 200), (250, 250), (300, 300),
                                  (350, 350), (400, 400)],
                   [(-50, -50), (-100, -100), (-150, -150), (-200, -200), (-250, -250),
                    (-300, -300), (-350, -350), (-400, -400)],
                   [(-50, 50), (-100, 100), (-150, 150), (-200, 200), (-250, 250), (-300, 300),
                    (-350, 350), (-400, 400)],
                   [(50, -50), (100, -100), (150, -150), (200, -200), (250, -250), (300, -300),
                    (350, -350), (400, -400)], [(0, 50)], [(50, 0)], [(0, -50)], [(-50, 0)]],
                  ['Pro Rook', [(0, 50), (0, 100), (0, 150), (0, 200), (0, 250), (0, 300), (0, 350), (0, 400)],
                   [(50, 0), (100, 0), (150, 0), (200, 0), (250, 0), (300, 0), (350, 0), (400, 0)],
                   [(-50, 0), (-100, 0), (-150, 0), (-200, 0), (-250, 0), (-300, 0), (-350, 0), (-400, 0)],
                   [(0, -50), (0, -100), (0, -150), (0, -200), (0, -250), (0, -300), (0, -350), (0, -400)], [(50, 50)],
                   [(50, -50)], [(-50, 50)], [(-50, -50)]]]

selection_order_temp_move_list = []
promotion = ["Pawn", "Knight", "Lance", "Bishop", "Rook"]
order_selected = []
king_danger = []
middle = mid()
turn_counter = 1

wn = turtle.Screen()
wn.title("Shogi")
make_board()
make_yards()
wn.register_shape("tri", ((10, -3), (10, -12), (-10, -12), (-10, -3), (-5, 10), (5, 10)))
highlighter = turtle.Turtle()
highlighter.ht()

for player_one_set in player_one:
    turtle_names = player_one_set[3]
    turtle_names.shape("tri")
    turtle_names.penup()
    turtle_names.setpos(player_one_set[1], player_one_set[2])
    turtle_names.left(90)
    turtle_names.write(player_one_set[0] + "\n", align="center", font=("Arial", 7, "bold"))

for player_two_set in player_two:
    turtle_names = player_two_set[3]
    turtle_names.shape("tri")
    turtle_names.penup()
    turtle_names.setpos(player_two_set[1], player_two_set[2])
    turtle_names.right(90)
    turtle_names.write(player_two_set[0] + "\n", align="center", font=("Arial", 7, "bold"))

if turn_counter == 1:
    wn.onclick(select)

wn.mainloop()