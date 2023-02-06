from doctest import ELLIPSIS_MARKER


a = float(input('a: '))

b = float(input('b: '))

c = float(input('c: '))

if a + b > c or a + c > b and b + c > a:
    if a == b == c:
        print('Kolmnurk on võrdkülgne')
    elif a == b or a == c or b == c:
        print('Kolmnurk on võrdhaarne')
    else:
        print('Kolmnurk on erikülgne')
else:
    print('Sellist kolmnurka ei saa joonestada')
