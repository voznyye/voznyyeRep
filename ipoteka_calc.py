import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--type')
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)

args = parser.parse_args()

list_diff = {args.principal, args.periods, args.interest}
list_payment = {args.periods, args.principal, args.interest}
list_principal = {args.periods, args.payment, args.interest}
list_month = {args.principal, args.payment, args.interest}


def overhueta():
    o = args.periods * args.payment
    o = math.ceil(o - args.principal)
    print(f'Overpayment = {o}')


def different():
    m = 0
    o = 0
    i = args.interest / 12 / 100
    for j in range(args.periods):
        m += 1
        args.payment = math.ceil(args.principal / args.periods + i *
                                 (args.principal - (args.principal * (m - 1)) / args.periods))
        print(f'Month {m}: payment is {args.payment}')
        o = o + args.payment
    o = o - args.principal
    print()
    print(f'Overpayment = {o}')


def payment():
    i = args.interest / 12 / 100
    args.payment = math.ceil(args.principal * ((i * math.pow(1 + i, args.periods)) /
                                               (math.pow(1 + i, args.periods) - 1)))
    print(f'Your monthly payment = {args.payment}!')
    overhueta()


def month():
    i = args.interest / 12 / 100
    args.periods = math.ceil((math.log(args.payment / (args.payment - i * args.principal), i + 1)))
    zaloopa(args.periods)
    overhueta()


def principal():
    i = args.interest / 12 / 100
    args.principal = math.floor(args.payment / ((i * math.pow(1 + i, args.periods)) /
                                                (math.pow(1 + i, args.periods) - 1)))
    print(f'Your loan principal = {args.principal}!')
    overhueta()


def zaloopa(m):
    y = 0
    for j in range(m):
        if m >= 12:
            y += 1
            m -= 12
    if m == 0 and y > 1:
        print(f'It will take {y} years to repay this loan!')
    if y == 0 and m > 1:
        print(f'It will take {m} months to repay this loan!')
    if m == 1 and y == 0:
        print(f'It will take {m} month to repay this loan!')
    if y == 1 and m == 0:
        print(f'It will take {y} year to repay this loan!')
    if m == 1 and y != 1:
        print(f'It will take {y} year and {m} months to repay this loan!')
    if m != 1 and y == 1:
        print(f'It will take {y} years and {m} month to repay this loan!')
    if m != 1 and y != 1:
        print(f'It will take {y} years and {m} months to repay this loan!')
    else:
        print(f'It will take {y} year and {m} month to repay this loan!')


if args.type == 'diff' and all(list_diff):
    different()
elif args.type == 'annuity' and all(list_payment):
    payment()
elif args.type == 'annuity' and all(list_month):
    month()
elif args.type == 'annuity' and all(list_principal):
    principal()
else:
    print('Incorrect parameters.')
