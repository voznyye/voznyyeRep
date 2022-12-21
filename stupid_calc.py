msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... stupid"
msg_7 = " ... very stupid"
msg_8 = " ... very, very stupid"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0.0



def is_one_digit(v):
    output = False
    if v.is_integer() and (-10 < v < 10):
        output = True
    return output


def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and (v3 == '*'):
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 != '/'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg

    print(msg)


def validate(x, oper, y):
    result = False

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
    else:
        if oper not in ['+', '-', '*', '/']:
            print(msg_2)
        else:
            check(x, y, oper)

            if oper == '/' and y == 0:
                print(msg_3)
            else:
                result = True

    return result


def calculate(x, oper, y):
    result = 0.0

    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        result = x / y
    print(result)

    return result


while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    if not validate(x, oper, y):
        continue

    result = calculate(float(x), oper, float(y))

    answer = ''
    while answer not in ['y', 'n']:
        print(msg_4)
        answer = input()
        if answer != 'y':
            continue

        if is_one_digit(result):
            print(msg_10)
            answer = input()
            if answer == 'y':
                print(msg_11)
                answer = input()
                if answer == 'y':
                    print(msg_12)
                    answer = input()
                    if answer == 'y':
                        memory = result

        else:
            memory = result

    answer = ''
    while answer not in ['y', 'n']:
        print(msg_5)
        answer = input()

    if answer == 'n':
        break