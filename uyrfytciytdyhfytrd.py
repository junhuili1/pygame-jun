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
    # put everything below this in a while loop or for loop just a loop
    fail = False
    lowestlast = [0, 10000000000000000000000]
    while True:
        if len(listofstartandlast) == 0:
            break
        if lowestlast == [0, 10000000000000000000000]:
            for i in listofstartandlast:
                if i[1] < lowestlast[1]:
                    lowestlast = i
            listofstartandlast.remove(lowestlast)
            lowestlast = lowestlast[1]
       #  print("lowestlast: " + str(lowestlast))

        workingfirst = [10000000000000000000000]
        for i in listofstartandlast:
            if i[0] > lowestlast and i[0] < workingfirst[0]:
                workingfirst = i
        #print("workingfirst: " + str(workingfirst[0]))
        if workingfirst[0] == 10000000000000000000000:
            fail = True
            break
        lowestlast = workingfirst[1]
       # print("newlowestlast: " + str(lowestlast))
        listofstartandlast.remove(workingfirst)
    if fail: print("NO")
    else: print("YES")
    
i = 0

while True:
    print("credit to jun batu and ben")
    WhyLena(2, [[2, 1, 3], [1, 2]])
    i+=1
    if i==100:
        break