def to_jaden_case(string):
    c = 0
    x = ''
    while c < len(string):
        if c == 0:
            x = x + string[0].upper()
            c = c + 1  
        if string[c] != ' ' and string[c-1] != ' ' :
            x = x + string[c]
        elif string[c] == ' ':
            x = x + ' '
            x = x + string[c+1].upper()
        c = c + 1    
    return x 


print(to_jaden_case(input('Write anything you want : ')))    


