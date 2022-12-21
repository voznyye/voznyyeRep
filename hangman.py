commands = ['results', 'exit', 'play']
start_msg = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit > '

letters = ['a', 'b', 'd', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 8
count_lose = 0
count_win = 0

print(f'H A N G M A N # {count} attempts')

while True:

    menu = input(start_msg)
    ran = input('\nSecret word > ')

    memory = []
    count = 8
    # ran = random.choice(answer)
    space = '-' * (len(ran))

    if menu == 'play':
        print()
        print(space)
        while True:
            guess = input('Input a letter > ')

            if len(guess) > 1 or guess == '':
                print('Please, input a single letter.\n')

            elif guess in memory and guess in letters:
                print("You've already guessed this letter.\n")

            elif guess not in letters or guess.isupper():
                print('Please, enter a lowercase letter from the English alphabet.\n')

            elif guess not in ran:
                count -= 1
                print(f"That letter doesn't appear in the word. # {count} attempts\n")

            memory.append(guess)

            if guess not in space and guess in ran:
                print()

            if guess in ran:
                con = -1
                for i in ran:
                    con += 1
                    if guess == i:
                        space = space[:con] + guess + space[con + 1:]

            if space == ran:
                count_win += 1
                print(space)
                print(f'You guessed the word {space}!\nYou survived!')
                break

            if count == 0:
                count_lose += 1
                print()
                print('You lost!')
                break
            print(space)
    if menu == 'results':
        print(f'You won: {count_win} times.\nYou lost: {count_lose} times.')
    if menu == 'exit':
        break
    if menu not in commands:
        pass
