def two_sum1(num,target):
    hashmap = {}
    list = []
    diff = 0

    for i in range(len(num)):
        diff = target - num[i]
        if diff in hashmap :
            list.append([hashmap[diff],i])
        hashmap[num[i]] = i

    return list

num = [2,7,6,5,1,8]
print(two_sum1(num,9))

