def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def dev(a, b):
    return a/b


def reverse(s):
    '''
    to reverse our string
    '''
    return s[::-1]

def isfloat(s):
    '''
    to check if string contains float number
    '''
    if '.' not in s:
        return False
    dot = s.index('.')
    left = s[0:dot]
    right = s[dot+1:len(s)]
    if left.isdigit() and right.isdigit():
        return True
    else:
        return False

s = input()

while True:
    res = None  # var for function which we'll use
    pos = 0     # var for position of arithmetic sign
    sign = ''
    num1, num2 = '', ''
    if '/' in s:
        sign = '/'
        res = dev
        pos = s.index('/')
    elif '*' in s:
        sign = '*'
        res = mul
        pos = s.index('*')
    elif '-' in s:
        sign = '-'
        res = sub
        pos = s.index('-')
    elif '+' in s:
        sign = '+'
        res = add
        pos = s.index('+')
    else:
        print(s)
        raise Exception('Invalid sign')     # in case if we'll get something else

    # defining number1

    for i in range(pos-1, -1, -1):
        if s[i].isdigit():
            num1+=s[i]
        elif s[i] == '.':
            num1+=s[i]
        else:
            break
    num1 = reverse(num1)

    if isfloat(num1):
        var1 = float
    else:
        var1 = int

    # defining number2

    for i in range(pos+1, len(s)):
        if s[i].isdigit():
            num2+=s[i]
        elif s[i] == '.':
            num2+=s[i]
        else:
            break

    if isfloat(num2):
        var2 = float
    else:
        var2 = int

    new = res(var1(num1), var2(num2))  # result of our operation
    old = num1 + sign + num2
    s = s.replace(old, str(new))

    if isfloat(s):     # Checking if there are only numbers in the string left
        break

print('Result:', s)