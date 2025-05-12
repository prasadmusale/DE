def are_anagrams (str1 , str2):
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    if len(str1) != len(str2) :
        return False 
    
    dict1 = {}
    dict2 = {}

    for i in str1 :
        if i in dict1 :
            dict1[i] += 1
        else :
            dict1[i] = 1

    for i in str2 :
        if i in dict2 :
           dict2[i] += 1
        else :
            dict2[i] = 1

    for key in dict1 :
        if key not in dict2 or dict1[key] != dict2[key] :
            return False 
        
    return True

print(are_anagrams("Listen","Silent"))
print(are_anagrams("hello","world"))