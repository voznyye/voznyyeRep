import random

inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8',  '-0', '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '']
status = ''
turn = 0
loop_snake = []

dominoes = stocks = [[i, j] for i in range(7) for j in range(i, 7)]
stock, comp_pieces, player_pieces, domino_snake, re_counter = [], [], [], [[0, 1]], []


def endgame():
    global status
    if not player_pieces:
        status = 'The game is over. You won!'
        print(f'Status: {status}')
        exit(0)
    if not comp_pieces:
        status = 'The game is over. The computer won!'
        print(f'Status: {status}')
        exit(0)


def comp_turn():
    for k in range(7):
        snake_count = sum(1 for i in loop_snake for j in i if j == k)
        comp_count = sum(1 for i in comp_pieces for j in i if j == k)
        re_counter.append(comp_count + snake_count)

    rating_list = []
    for j in range(15):
        for i in comp_pieces:
            if re_counter[i[0]] + re_counter[i[1]] == j:
                rating_list.insert(0, i)

    for i in rating_list:
        c = 0
        if loop_snake[-1][-1] == i[0]:
            loop_snake.append(comp_pieces.pop(comp_pieces.index(i)))
            return
        elif loop_snake[-1][-1] == i[1]:
            x = comp_pieces.pop(comp_pieces.index(i))
            x.reverse()
            loop_snake.append(x)
            return
        elif loop_snake[0][0] == i[1]:
            loop_snake.insert(0, comp_pieces.pop(comp_pieces.index(i)))
            return
        elif loop_snake[0][0] == i[0]:
            x = comp_pieces.pop(comp_pieces.index(i))
            x.reverse()
            loop_snake.insert(0, x)
            return

    for j in comp_pieces:
        if loop_snake[-1][-1] != j[0] and loop_snake[-1][-1] != j[1] and \
                    loop_snake[0][0] != j[1] and loop_snake[0][0] != j[0]:
            c += 1
            break
    if c != 0:
        if len(stock) == 0:
            return
        else:
            comp_pieces.append(stock.pop(random.randint(0, len(stock) - 1)))
            c = 0


def player_turn():

    if move == '0':
        if len(stock) == 0:
            return
        else:
            player_pieces.append(stock.pop(random.randint(0, len(stock) - 1)))

    elif move.isdigit():
        if loop_snake[-1][-1] == player_pieces[int(move) - 1][0]:
            loop_snake.append(player_pieces.pop(int(move) - 1))

        elif loop_snake[-1][-1] == player_pieces[int(move) - 1][1]:
            y = player_pieces.pop(int(move) - 1)
            y.reverse()
            loop_snake.append(y)

    elif move[0] == '-' and move[1].isdigit():
        if loop_snake[0][0] == player_pieces[int(move[1]) - 1][1]:
            loop_snake.insert(0, player_pieces.pop(int(move[-1]) - 1))

        elif loop_snake[0][0] == player_pieces[int(move[1]) - 1][0]:
            y = player_pieces.pop(int(move[-1]) - 1)
            y.reverse()
            loop_snake.insert(0, y)


def start_turn():
    global status, turn
    if len(comp_pieces) > len(player_pieces):
        turn = 1
        status = 'Computer is about to make a move. Press Enter to continue...'
        print(f'Status: {status}')
    else:
        turn = 0
        status = "It's your turn to make a move. Enter your command."
        print(f'Status: {status}')


def your_pieces():
    c = 0
    print('Your pieces:')
    for i in player_pieces:
        c += 1
        print(f'{c}:{i}')
    print()


def shuffling():
    global stock, comp_pieces, player_pieces

    random.shuffle(dominoes)

    stock = dominoes[:14]
    comp_pieces = dominoes[14:21]
    player_pieces = dominoes[21:]


def choose_snake():
    global domino_snake, comp_pieces, player_pieces

    for i in player_pieces:
        if i[0] == i[1]:
            domino_snake.append(i)

    for i in comp_pieces:
        if i[0] == i[1]:
            domino_snake.append(i)

    if max(domino_snake)[0] != max(domino_snake)[1]:
        shuffling()
        choose_snake()

    if max(domino_snake) in comp_pieces:
        comp_pieces.remove(max(domino_snake))
    if max(domino_snake) in player_pieces:
        player_pieces.remove(max(domino_snake))


def main():
    print('=' * 70)

    print(f'Stock size: {len(stock)}')
    print(f'Computer pieces: {len(comp_pieces)}\n')
    if len(loop_snake) < 6:
        print(*loop_snake, sep='')
        print()
    else:
        print(*loop_snake[:3], '...', *loop_snake[-3:], sep='')
        print()

    your_pieces()


shuffling()
choose_snake()
loop_snake.append(max(domino_snake))
main()
start_turn()

while True:
    while True:
        move = input()
        if move not in inputs:
            print('Invalid input. Please try again.')
        elif move == '' and turn or move == '0':
            break
        elif loop_snake[-1][-1] != player_pieces[int(move[-1]) - 1][0] and\
                loop_snake[-1][-1] != player_pieces[int(move[-1]) - 1][1] and\
                loop_snake[0][0] != player_pieces[int(move[-1]) - 1][1] and \
                loop_snake[0][0] != player_pieces[int(move[-1]) - 1][0]:
            print('Illegal move. Please try again.')
        else:
            break
    if turn:
        turn = 0
        comp_turn()
    else:
        turn = 1
        player_turn()

    main()
    endgame()

    if turn:
        status = 'Computer is about to make a move. Press Enter to continue...'
        print(f'Status: {status}')
    else:
        status = "It's your turn to make a move. Enter your command."
        print(f'Status: {status}')
