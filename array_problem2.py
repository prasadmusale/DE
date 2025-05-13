def fun(num,target) :
    size = len(num)
    num1 = []
    inserted  = False
    for i in range(size) :
       if target < num[i] and inserted == False:
           num1.append(target)
           inserted = True
           num1.append(num[i])

       else :
           num1.append(num[i])
    return num1


num = [3,6,8,12,15]
print(fun(num,7))
