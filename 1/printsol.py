
def reverse(string):
    string = string[::-1]
    return string

with open("input") as file:
    m = 0
    for line in file:
        for c in line:
            if (c.isdigit()):
                i = c
                break
        for c in reverse(line):
            if (c.isdigit()):
                k = c
                break
        m += int(i+k)        
# print(m)

with open("input") as file:
    m = 0
    for line in file:
        i = 0
        k = 0
        for c in line:
            if (c.isdigit()):
                i = c
                break
            else
                #something
        for c in reverse(line):
            if (c.isdigit()):
                k = c
                break
            else
                #something
        m += int(i+k)        
print(m) #9883