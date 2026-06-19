import turtle, random

t1 = turtle.Turtle()
screen = turtle.Screen()
t1.speed(0)
t1.hideturtle()

y = 250
for i in range(3):
    x = -150
    y -= 100
    for j in range(3):
        t1.penup()
        t1.goto(x, y)
        t1.pendown()
        t1.setheading(270)
        for _ in range(4):
            t1.forward(100)
            t1.left(90)
        x += 100

t1.penup()

list_cells = [0,0,0,
              0,0,0,
              0,0,0]
turn = [random.choice(['cross', 'zero'])]
game_over = False

def zero(x, y):
    t1.penup()
    t1.goto(x + 50, y - 100)
    t1.setheading(0)
    t1.pendown()
    t1.circle(50)
    turn[0] = 'cross'

def cross(x, y):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.goto(x + 100, y - 100)
    t1.penup()
    t1.goto(x + 100, y)
    t1.pendown()
    t1.goto(x, y - 100)
    t1.penup()
    turn[0] = 'zero'

index_cell = [0]
xs = [0]
ys = [0]

def check_cell(x, y):
    if -150 <= x < -50:
        col = 0
        xs[0] = -150
    elif -50 <= x < 50:
        col = 1
        xs[0] = -50
    elif 50 <= x < 150:
        col = 2
        xs[0] = 50
    else:
        return False

    if 150 >= y > 50:
        row = 0
        ys[0] = 150
    elif 50 >= y > -50:
        row = 1
        ys[0] = 50
    elif -50 >= y > -150:
        row = 2
        ys[0] = -50
    else:
        return False

    index_cell[0] = row * 3 + col
    return True

def on_click(x, y):
    global game_over
    if game_over or not check_cell(x, y):
        return

    if list_cells[index_cell[0]] == 0:
        list_cells[index_cell[0]] = turn[0]

        if turn[0] == "cross":
            cross(xs[0], ys[0])
        elif turn[0] == "zero":
            zero(xs[0], ys[0])

        check_victory()

def draw_line(start_index, end_index):
    x_coords = [-150, -50, 50]
    y_coords = [150, 50, -50]
    x1 = x_coords[start_index % 3] + 50
    y1 = y_coords[start_index // 3] - 50
    x2 = x_coords[end_index % 3] + 50
    y2 = y_coords[end_index // 3] - 50
    t1.penup()
    t1.goto(x1, y1)
    t1.pendown()
    t1.pensize(4)
    t1.color("green")
    t1.goto(x2, y2)

def check_victory():
    global game_over
    victories = [[0,1,2],[3,4,5],[6,7,8],
                 [0,3,6],[1,4,7],[2,5,8],
                 [0,4,8],[2,4,6]]

    for a, b, c in victories:
        if list_cells[a] == list_cells[b] == list_cells[c] != 0:
            game_over = True
            winner = 'Нолик' if list_cells[a] == 'zero' else 'Крестик'
            t1.penup()
            t1.goto(0, 200)
            t1.pendown()
            t1.color("green")
            t1.write(f"Победил {winner}", font=("Arial", 24))
            draw_line(a, c)
            return

    if list_cells.count(0) == 0:
        game_over = True
        t1.penup()
        t1.goto(-150, 0)
        t1.pendown()
        t1.pensize(4)
        t1.penup()
        t1.goto(-40, 200)
        t1.color("red")
        t1.pendown()
        t1.write("Ничья!", font=("Arial", 24))



























screen.onclick(on_click)
turtle.mainloop()
