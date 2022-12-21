turn = 0
pos = '_________'
link = list(pos)
tab = [
    [link[0], link[1], link[2]],
    [link[3], link[4], link[5]],
    [link[6], link[7], link[8]]
]


def win_x():
    if pabeda[0:3] == 'XXX' or pabeda[3:6] == 'XXX' or pabeda[6:-1] == 'XXX' or pabeda[0:7:2] == 'XXX' or \
            pabeda[1:8:2] == 'XXX' or pabeda[2:-1:2] == 'XXX' or pabeda[0:-1:3] == 'XXX' or pabeda[2:7:1] == 'XXX':
        return 0


def win_o():
    if pabeda[0:3] == 'OOO' or pabeda[3:6] == 'OOO' or pabeda[6:-1] == 'OOO' or pabeda[0:7:2] == 'OOO' or \
            pabeda[1:8:2] == 'OOO' or pabeda[2:-1:2] == 'OOO' or pabeda[0:-1:3] == 'OOO' or pabeda[2:7:1] == 'OOO':
        return 0


def grid():
    print("---------")
    print(f"| {tab[0][0]} {tab[0][1]} {tab[0][2]} |")
    print(f"| {tab[1][0]} {tab[1][1]} {tab[1][2]} |")
    print(f"| {tab[2][0]} {tab[2][1]} {tab[2][2]} |")
    print("---------")


while True:
    turn += 1
    link = sum(tab, [])
    pabeda = ''.join(link)
    if win_x() == 0:
        print('X wins')
        break
    if win_o() == 0:
        print('O wins')
        break
    if turn % 2 != 0:
        mark = 'X'
    else:
        mark = 'O'

    coord = input()

    n = [x for x in coord.split() if x.isalpha()]
    if len(n) > 0:
        turn -= 1
        print("You should enter numbers!")
    else:
        row, col = coord.split()
        row, col = int(row), int(col)
        nums = [1, 2, 3]
        if row not in nums or col not in nums:
            turn -= 1
            print("Coordinates should be from 1 to 3!")
        elif tab[row - 1][col - 1] == "_":
            tab[row - 1][col - 1] = mark
            grid()
        elif tab[row - 1][col - 1] != " ":
            print("This cell is occupied! Choose another one!")
    if turn == 10:
        print('Draw')
        break
