def remove_outer_layer(str):
    s = ''
    for i in range(len(str)-1):
        if str[i] == '(':
            if str[i+1] == ')':
                s += str[i]+str[i+1]
    return s
if __name__ == '__main__':
    str = input(" - ")
    print(remove_outer_layer(str))