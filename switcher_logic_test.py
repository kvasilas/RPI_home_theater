current = 2
target = 1

def switch(target, current):
    #get current
    while(target != current):
        if(current == 3):
            current = 1
        else:
            current += 1
        #button press
        print('button press')
        #get current
        print(current, target, sep=' / ')
    return()
#switch(target, current)

string = 'penis'
print(string[0])
string = 'gobbler' + string
print(string)
