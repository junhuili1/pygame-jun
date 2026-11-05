def WhyLena(boxnum, lol):
    workingbox = True
    for i in range(boxnum):
        for i2 in range(lol[i][0]-1):
            if lol[i][i2+1] > lol[i][i2+2]:
                workingbox = False
                break
        if not workingbox:
            break
    if not workingbox:
        print("NO")
        return
    listofstartandlast = []
    for i in lol:
        if len(i) == 2:
            listofstartandlast.append([i[1], i[1]])
        else:
            listofstartandlast.append([i[1], i[len(i)-1]])
    print(listofstartandlast)
WhyLena(3, [[2, 1, 2], [3, 7, 7, 7], [1, 5]])