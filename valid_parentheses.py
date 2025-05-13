def valid_parenthesis(str) :
    stack = []
    dict = {"(":")" , "[":"]","{":"}"}
    for i in str :
        if i in dict.keys():
            stack.append(i)
        elif i in dict.values() :
            if dict[stack[-1]] == i :
                stack.pop()
            else :
                return False 
    if len(stack) == 0 :
        return True
    else :
        return False
    
print(valid_parenthesis("()"))
print(valid_parenthesis("()[]{}"))
print(valid_parenthesis("(]"))
print(valid_parenthesis("([)]"))
print(valid_parenthesis("{[]}"))