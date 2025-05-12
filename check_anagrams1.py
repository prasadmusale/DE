def are_anagrams1(str1 , str2) :
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())

    if str1 == str2 :
        return True
    else :
        return False

print(are_anagrams1("Listen","Silent"))
print(are_anagrams1("Hello","World"))