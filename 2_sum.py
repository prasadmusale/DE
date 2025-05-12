def two_sum(num , target) :
    n = len(num)
    list1 = []
    for i in range(n) :
        for j in range(i+1,n):
            if(num[i]+num[j] == target) :
                 list1.append([i,j])
    return list1

num = [2,7,11,15,1,8]
target = 9

print(two_sum(num,target))