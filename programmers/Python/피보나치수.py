def solution(n):
    i = 2
    prenum = 1
    prePrenum = 0

    for i in range(2,n+1):
        Fibon = prePrenum + prenum
        prePrenum = prenum
        prenum = Fibon

    return Fibon % 1234567
