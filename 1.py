def zadacha1(a):
    if int(a) % 3 == 0:
        return print("Делится")
    else:
        return print("Не делится")

def zadacha2(a):
    if a == 0:
        return print("На ноль делит нельзя")
    elif isinstance(a, int):
        return print("Не число")
    else:
        return print(100/int(a))

def zadacha3(a):
    chislo1=a[0]+a[1]
    chislo2=a[3]+a[4]
    chislo3=a[-2]+a[-1]
    if int(chislo1)*int(chislo2) == int(chislo3):
        return print("Дата магическая")
    else:
        return print("Дата не магическая")

def zadacha4(a):
    symbols = [symbol for symbol in a]
    j=0
    chislo1=0
    chislo2=0
    for i in symbols:
        if j<len(a)/2:
            chislo1=chislo1+int(i)
        else:
            chislo2=chislo2+int(i)
        j=j+1
    if chislo1==chislo2:
        return print("Число магическое")
    else:
        return print("Число не магическое")

a=input("Введите число")
zadacha4(a)