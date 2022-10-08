from cmath import pi

end = False
while not (end):
    p = float(input('Escribe un parametro para el circulo '))
    pi
    d = p / pi
    si_no = input('quieres sacar el radio? Y/N: ')
    if si_no == 'n':
        print(d)
        end = True
    elif si_no == 'y':
        r = d / 2
        print(r)
        end = True
    else:
        print('error')

# circulo