lenth=int(input("Введите длину\n"))
width=int(input("Введите ширину\n"))
count=65
doplenth=lenth
dopwidth=width
matrix=['0']*width
for i in range(width):
    matrix[i]=['0']*lenth
def CutSquare(len, wid, count, doplenth, dopwidth):

    if len>wid:
        print("Отрезан квадрат "+str(wid)+"x"+str(wid))
#        list=['0']*wid
#        for i in range(wid):
#            list[i]=['0']*wid
#        for i in range(wid):
#            for j in range(wid):
#                list[i][j]=chr(count)
        for i in range(dopwidth-wid, dopwidth):
            for j in range(doplenth-len, doplenth-len+wid):
                matrix[i][j]=chr(count)
        if count-64==65:
            count=65
        else:
            count+=1
#        for i in range(wid):
#            for j in range(wid):
#                print(list[i][j], end=' ')
#            print()
        len-=wid
        CutSquare(len, wid, count, doplenth, dopwidth)
    elif len==wid:
        if count==65:
            print("Вы ввели квадрат "+str(len)+"x"+str(wid))
#            list=['0']*wid
#            for i in range(wid):
#                list[i]=['0']*wid
#            for i in range(wid):
#                for j in range(wid):
#                    list[i][j]=chr(count)
#            for i in range(wid):
#                for j in range(wid):
#                   print(list[i][j], end=' ')
#                print()
        else:
            print("Отрезан квадрат "+str(wid)+"x"+str(wid))
            for i in range(dopwidth-wid, dopwidth):
                for j in range(doplenth-len, doplenth):
                    matrix[i][j]=chr(count)
        return
    else:
        wid-=len
        print("Отрезан квадрат "+str(len)+"x"+str(len))
#        list=["0"]*len
#        for i in range(len):
#            list[i]=["0"]*len
#        for i in range(len):
#            for j in range(len):
#                list[i][j]=chr(count)
        for i in range(dopwidth-len, dopwidth):
            for j in range(doplenth-len, doplenth):
                matrix[i][j]=chr(count)
        dopwidth-=len
        if count-64==65:
            count=65
        else:
            count+=1
#        for i in range(len):
#            for j in range(len):
#                print(list[i][j], end=' ')
#            print()
        CutSquare(len, wid, count, doplenth, dopwidth)
CutSquare(lenth, width, count, doplenth, dopwidth)
for i in range(width):
    for j in range(lenth):
        print(matrix[i][j], end=' ')
    print()