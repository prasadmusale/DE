def occurence(str) :
    hashmap = {}
     
    for i in str :
      if i in hashmap :
         hashmap[i] += 1
      else :
         hashmap[i] = 1

    return hashmap

str = "My name is Prasad"
print(occurence(str))
   