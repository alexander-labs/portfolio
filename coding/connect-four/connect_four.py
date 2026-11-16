# This code was made by Gemini because it would take forever to type out all of the commands just to draw a cute trophy at the end. My actual code...
#...starts at line 112.

import turtle

def draw_trophy(x=0, y=0, scale=1.0, speed=5):
    """
    Draws a curved gold trophy centered around (x, y) at a given scale.
    Self-contained: creates its own turtle and cleans up its state when done.
    """
    t = turtle.Turtle()
    t.speed(speed)
    t.hideturtle()

    def pt(px, py):
        """Scales and offsets local coordinates to (x, y)."""
        return (x + px * scale, y + py * scale)

    def bezier_curve(p0, p1, p2, steps=25):
        """Moves the turtle along a smooth quadratic curve."""
        x0, y0 = pt(*p0)
        x1, y1 = pt(*p1)
        x2, y2 = pt(*p2)
        for i in range(1, steps + 1):
            u = i / steps
            bx = (1 - u)**2 * x0 + 2 * (1 - u) * u * x1 + u**2 * x2
            by = (1 - u)**2 * y0 + 2 * (1 - u) * u * y1 + u**2 * y2
            t.goto(bx, by)

    # 1. Draw Curved Handles
    t.color("goldenrod")
    t.width(max(1, 7 * scale))

    # Left handle
    t.penup()
    t.goto(pt(-62, 125))
    t.pendown()
    bezier_curve((-62, 125), (-115, 115), (-95, 70))
    bezier_curve((-95, 70), (-80, 40), (-45, 45))

    # Right handle
    t.penup()
    t.goto(pt(62, 125))
    t.pendown()
    bezier_curve((62, 125), (115, 115), (95, 70))
    bezier_curve((95, 70), (80, 40), (45, 45))

    # 2. Draw Curved Gold Cup and Flared Stem
    t.width(max(1, 3 * scale))
    t.color("goldenrod", "gold")
    t.begin_fill()

    t.penup()
    t.goto(pt(-70, 145))
    t.pendown()
    bezier_curve((-70, 145), (0, 138), (70, 145))
    bezier_curve((70, 145), (65, 50), (14, 15))
    bezier_curve((14, 15), (10, -25), (42, -65))
    t.goto(pt(-42, -65))
    bezier_curve((-42, -65), (-10, -25), (-14, 15))
    bezier_curve((-14, 15), (-65, 50), (-70, 145))

    t.end_fill()

    # 3. Draw Top Rim Highlight
    t.color("#b8860b")
    t.width(max(1, 3 * scale))
    t.penup()
    t.goto(pt(-68, 138))
    t.pendown()
    bezier_curve((-68, 138), (0, 131), (68, 138))

    # 4. Draw Dark Pedestal Base
    t.color("black", "#2c2c2c")
    t.begin_fill()

    t.penup()
    t.goto(pt(-52, -65))
    t.pendown()
    t.goto(pt(52, -65))
    t.goto(pt(64, -105))
    t.goto(pt(-64, -105))
    t.goto(pt(-52, -65))

    t.end_fill()

    # 5. Draw Gold Nameplate
    t.color("goldenrod", "gold")
    t.begin_fill()

    t.penup()
    t.goto(pt(-34, -75))
    t.pendown()
    t.goto(pt(34, -75))
    t.goto(pt(34, -95))
    t.goto(pt(-34, -95))
    t.goto(pt(-34, -75))

    t.end_fill()

# This is the rest of the code I actually made.

c4Board = [
    ['. ','. ','. ','. ','. ','. ','. ',],
    ['. ','. ','. ','. ','. ','. ','. ',],
    ['. ','. ','. ','. ','. ','. ','. ',],
    ['. ','. ','. ','. ','. ','. ','. ',],
    ['. ','. ','. ','. ','. ','. ','. ',],
    ['. ','. ','. ','. ','. ','. ','. ',],
    ]

def print_board(c4Board):
    '''Prints the Connect Four board'''
    print('0 1 2 3 4 5 6 ')
    for r in range(6):
        for c in range(7):
            print(c4Board[r][c], end='')
        print('\n')

def win_check(c4Board):
    '''Checks all possible win positions in Connect Four for X and O.'''
    for r in range(6):
        for c in range(4):
            if c4Board[r][c] == c4Board[r][c+1] == c4Board[r][c+2] == c4Board[r][c+3] == 'X ':
                return 'X wins'
            if c4Board[r][c] == c4Board[r][c+1] == c4Board[r][c+2] == c4Board[r][c+3] == 'O ':
                return 'O wins'
    for r in range(3):
        for c in range(7):
            if c4Board[r][c] == c4Board[r+1][c] == c4Board[r+2][c] == c4Board[r+3][c] == 'X ':
                return 'X wins'
            if c4Board[r][c] == c4Board[r+1][c] == c4Board[r+2][c] == c4Board[r+3][c] == 'O ':
                return 'O wins'
    for r in range(3):
        for c in range(0,4):
            if c4Board[r][c] == c4Board[r+1][c+1] == c4Board[r+2][c+2] == c4Board[r+3][c+3] == 'X ':
                return 'X wins'
            if c4Board[r][c] == c4Board[r+1][c+1] == c4Board[r+2][c+2] == c4Board[r+3][c+3] == 'O ':
                return 'O wins'
    for r in range(3):
        for c in range(3,7):
            if c4Board[r][c] == c4Board[r+1][c-1] == c4Board[r+2][c-2] == c4Board[r+3][c-3] == 'X ':
                return 'X wins'
            if c4Board[r][c] == c4Board[r+1][c-1] == c4Board[r+2][c-2] == c4Board[r+3][c-3] == 'O ':
                return 'O wins'
# Note that X would have the advantage if both X and O got a 4-in-a-row on the same turn. However, that's impossible because X moves first anyways, so that's not an issue.


while True: # Now time to actually play the game!
    print_board(c4Board)
    pXMove = int(input('Player X, select your column: '))
    for i in range(5,-1,-1):
        if c4Board[i][pXMove] == '. ':
            c4Board[i][pXMove] = 'X '
            break
        if i == 0:
            print('You played in an already full column, buddy. I dont mean to be toxic, but you lost your turn.')
        
    if win_check(c4Board) == 'X wins':
        print('CONGRATULATIONS TO X FOR WINNING THIS YEARS CONNECT 4 WORLD CUP! HERE IS YOUR TROPHY!')
        print_board(c4Board)
        draw_trophy(x=0, y=0, scale=1.0, speed=5)
        turtle.done()
        break
    print_board(c4Board)
    
    pOMove = int(input('Player O, select your column: '))
    for j in range(5,-1,-1):
        if c4Board[j][pOMove] == '. ':
            c4Board[j][pOMove] = 'O '
            break
        if j == 0:
            print('You played in an already full column, buddy. I dont mean to be toxic, but you lost your turn.')

    if win_check(c4Board) == 'O wins':
        print('CONGRATULATIONS TO O FOR WINNING THIS YEARS CONNECT 4 WORLD CUP! HERE IS YOUR TROPHY!')
        print_board(c4Board)
        draw_trophy(x=0, y=0, scale=1.0, speed=5)
        turtle.done()
        break