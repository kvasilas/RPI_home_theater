import os
ser = 'hello'

def write():
    print('temp_start')
    global ser
    ser= 'bye'
def read():
    print(ser)

write()
read()

print(os.getcwd())

# def lists():
#     words = ['a', 'b']
#     words.append('c')
#     print(words)
#
#
#     #make iteration through list more clean and pretty
#     for x in range(len(words)):
#         print(words[x])
#
#     del words[2]
#     print(words)
#     print(len(wrods))
#
# def sdsd():
#     str = 'https://www.amazon.com/The-Tick/dp/B01J776HVW'
#     if 'amazon' in str:
#         print('yay')
#     list = ['https://www.amazon.com/The-Tick/dp/B01J776HVW', 'https://www.sonycrackle.com/the-tick']
#     keys = ['netflix', 'amazon', 'hulu', 'crackle']
#     buttons = []
#
#     for i in range(len(list)):
#         for j in range(len(keys)):
#             if keys[j] in list[i]:
#                 buttons.append(keys[j])
#     print(buttons)
#
#
#
# sdsd()
