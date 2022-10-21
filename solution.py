def isValid(nput):
    checked_string = ''
    dict = {'(' : ')', '[' : ']', '{' : '}'}
    check = []
    for i in nput:
        if i in dict.keys() or i in dict.values():
            checked_string += i
    if len(checked_string) % 2 != 0:
        return False
    elif len(checked_string) > 0:
        for i in checked_string:
            if i in dict:
                check.append(i)
            else:
                if check == []:
                    return False
                a = check.pop()
                if i != dict[a]:
                    return False
        return check == []
    else:
        return False

print(isValid("(ad)[fas]a[asda]a"))
print(isValid("()][]"))
print(isValid(""))