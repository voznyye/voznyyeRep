counter = 0
posible_list = []
memory = []
star_poses = []
moves = [[2, 1], [-2, -1], [2, -1], [-2, 1], [1, 2], [-1, 2], [-1, -2], [1, -2]]


def moving():
    visited = 0
    while True:
        visited += 1
        try:
            star_counter = [[j.count('*') for j in i] for i in matrix]
            star_num = [sum(i) for i in star_counter]
            if sum(star_num) == (rows * cols):
                print('What a great tour! Congratulations!')
                exit(0)
            if not posible_list:
                print(f'No more possible moves!\nYour knight visited {visited} squares!')
                exit(0)

            move = input('Enter your next move: ')
            col_move, row_move = move.split()
            col_move, row_move = int(col_move) - 1, int(row_move) - 1
            if [col_move, row_move] in memory:
                print('hui')
                print(memory)
            if [col_move, row_move] in memory or [col_move, row_move] not in posible_list:
                print('Invalid move!', end=" ")
            else:
                posible_list.clear()
                posible_moves(row_move, col_move)
                memory.append([col_move, row_move])

        except (IndexError, ValueError):
            pass


def posible_moves(row, col):
    for i in moves:
        con = -1
        try:
            if (rows-1 - row + i[0] >= 0) and (col + i[1] >= 0) and (rows-1 - row + i[0] <= rows) and (col + i[1] <= cols):
                for x in moves:
                    if (rows-1 - row + i[0] + x[0] >= 0) and (col + i[1] + x[1] >= 0) and (rows-1 - row + i[0] + x[0] < rows) and (col + i[1] + x[1] < cols):
                        if '*' not in matrix[(rows-1 - row) + i[0]][col + i[1]]:
                            con += 1
                            matrix[(rows-1 - row) + i[0]][col + i[1]] = ((lens_str - 1) * ' ') + str(con)
                if '*' not in matrix[(rows-1 - row) + i[0]][col + i[1]]:
                    posible_list.append([col + i[1], row - i[0]])
        except IndexError:
            pass
    matrix[(rows-1) - row][col] = ((lens_str - 1) * ' ') + 'X'

    grid()
    for i in moves:
        try:
            matrix[(rows-1 - row) + i[0]][col + i[1]] = lens_str * '_'
        except IndexError:
            pass
    star_poses.append([(rows-1) - row, col])
    for i in star_poses:
        matrix[i[0]][i[1]] = ((lens_str - 1) * ' ') + '*'


def ch_pos():
    while True:
        try:
            cords = input("Enter the knight's starting position: ")
            col, row = cords.split()
            col, row = int(col) - 1, int(row) - 1
            memory.append([col, row])

            if 0 > col or 0 > row:
                print('Invalid dimensions!')
            else:
                posible_moves(row, col)
                break
        except (ValueError, IndexError):
            print('Invalid dimensions!')
    return counter + 1


def grid():
    a = rows

    if a >= 10:
        print(f'  {borders_num * "-"}')
        print(f"{a}| {' '.join(matrix[0][::])} |")
        for i in range(1, rows):
            a -= 1
            print(f" {a}| {' '.join(matrix[i][::])} |")
        print(f'  {borders_num * "-"}')
        nums = [' ' * (lens_str-1) + str(n) if len(str(n)) == 2 else ' ' * lens_str + str(n) for n in range(1, cols+1)]
        print(f"   {''.join(nums)}")
        print()
    else:
        print(f' {borders_num * "-"}')
        for i in range(rows):
            print(f"{a}| {' '.join(matrix[i][::])} |")
            a -= 1
        print(f' {borders_num * "-"}')
        nums = [' ' * (lens_str-1) + str(n) if len(str(n)) == 2 else ' ' * lens_str + str(n) for n in range(1, cols+1)]
        print(f"  {''.join(nums)}")
        print()


while True:
    try:
        size = input('Enter your board dimensions: ')
        cols_str, rows_str = size.split()
        cols, rows = int(cols_str), int(rows_str)

        if (len(cols_str) > 2 or len(rows_str) > 2) or (0 >= cols or 0 >= rows):
            print('Invalid dimensions!')
            continue
        lens_str = (len(str(rows * cols)))
        borders_num = cols * (lens_str + 1) + 3

        matrix = [[('_' * lens_str) for i in range(cols)] for j in range(rows)]

        if ch_pos():
            break

    except ValueError:
        print('Invalid dimensions!')
    except IndexError:
        print('Invalid position!')

moving()
