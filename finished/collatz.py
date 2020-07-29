def aLook (visitA, a):
    aCount = 0

    while a > 1:
        aCount += 1
        if a & 1:
            a = (a * 3) + 1
        else:
            a //= 2

        if a not in visitA:
            visitA[a] = aCount


def bLook (visitA, b):
    bCount = 0
    if b not in visitA:
        while b > 1:
            bCount += 1
            if b & 1:
                b = (b * 3) + 1
            else:
                b //= 2

            if b in visitA:
                return b, bCount
    return b, bCount

while 1:
    a, b = input().split()
    a, b = int(a), int(b)

    if a == 0 and b == 0:
        break

    visitA = {a: 0}

    aLook(visitA, a)
    tmp = bLook(visitA, b)

    print("%i needs %i steps, %i needs %i steps, they meet at %i" % (a, visitA[tmp[0]], b, tmp[1], tmp[0]))
