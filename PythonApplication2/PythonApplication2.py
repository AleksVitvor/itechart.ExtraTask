lenth=int(input("Введите длину\n"))
width=int(input("Введите ширину\n"))
count=65
def CutSquare(len, wid, count):

    if len>wid:
        len-=wid
        print("Отрезан квадрат "+str(wid)+"x"+str(wid))
        list=['0']*wid
        for i in range(wid):
            list[i]=['0']*wid
        for i in range(wid):
            for j in range(wid):
                list[i][j]=chr(count)
        if count-64==65:
            count=65
        else:
            count+=1
        for i in range(wid):
            for j in range(wid):
                print(list[i][j], end=' ')
            print()

        CutSquare(len, wid, count)
    elif len==wid:
        if count==65:
            print("Вы ввели квадрат "+str(len)+"x"+str(wid))
            list=['0']*wid
            for i in range(wid):
                list[i]=['0']*wid
            for i in range(wid):
                for j in range(wid):
                    list[i][j]=chr(count)
            for i in range(wid):
                for j in range(wid):
                    print(list[i][j], end=' ')
                print()
        return
    else:
        wid-=len
        print("Отрезан квадрат "+str(len)+"x"+str(len))
        list=["0"]*len
        for i in range(len):
            list[i]=["0"]*len
        for i in range(len):
            for j in range(len):
                list[i][j]=chr(count)
        if count-64==65:
            count=65
        else:
            count+=1
        for i in range(len):
            for j in range(len):
                print(list[i][j], end=' ')
            print()
        CutSquare(len, wid, count)
CutSquare(lenth, width, count)