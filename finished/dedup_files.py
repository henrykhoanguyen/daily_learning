
def getHash(file):
    hash = 0
    for c in file:
        hash ^= ord(c)
    return hash

while 1:
    num = int(input())
    if num == 0:
        break

    files = {}  # store only unique files
    numFiles = num
    dic = {}    # hash an unique number for each file
    numCollision = 0

    while num > 0:
        file = input()
        if file not in files:
            files[file] = 1
        else:
            files[file] += 1
        num -= 1

    for i in files:
        dic[i] = getHash(i)

    for i in files:
        for j in files:
            # to avoid making duplicate comparision
            if not (j == i):
                if dic[i] == dic[j]:
                    # if there is collision in hash, multiply number of file's occurrence
                    numCollision += files[i] * files[j]

    print(len(files), numCollision//2)
