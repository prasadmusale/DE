#There are two arrays merge both arrays in ascending order 

list1 = [7,5,1,10,9]
list2 = [3,8,2,6,4]
list3 = []

#Bubble sort 
for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j] :
            list1[i],list1[j] = list1[j],list1[i]

for i in range(len(list2)-1):
    for j in range(i+1,len(list2)):
        if list2[i] > list2[j] :
            list2[i],list2[j] = list2[j],list2[i]

i = 0
j = 0

while(i<len(list1) and j<len(list2)):
      if list1[i] < list2[j] :
        list3.append(list1[i])
        i += 1
      else :
        list3.append(list2[j])
        j += 1

while i<len(list1):
    list3.append(list1[i])
    i += 1

while j<len(list2):
    list3.append(list2[j])
    j += 1

print(list3)


