worDic = {}
numDic = {}
operator = ["-", "+"]
isPlus = True


def unknow(command):
    print(" ".join(command[1:]), "unknown")


while 1:
    command = input().split()

    if command[0] == "clear":
        break
    if command[0] == "def":
        worDic[command[1]] = int(command[2])
        numDic[int(command[2])] = command[1]
        # print("def")
    else:
        if not worDic:
            unknow(command)
        else:
            res = 0

            for i in command[1:]:
                if i == "=":
                    break
                if i not in worDic and i not in operator:
                    unknow(command)
                    res = None
                    break

                if i in worDic:
                    if isPlus:
                        res = res + worDic[i]
                    else:
                        res = res - worDic[i]
                elif i in operator:
                    if i == "-":
                        isPlus = False
                    else:
                        isPlus = True
            isPlus = True
            if res:
                if res in numDic:
                    print(" ".join(command[1:]), numDic[res])
                else:
                    unknow(command)
