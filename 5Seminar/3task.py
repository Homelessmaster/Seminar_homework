import random

list = []
textOutput = ''
dictionary = \
    {
        1: 'a',  2: 'b',
        3: 'c',  4: 'd',
        5: 'e',  6: 'f',
        7: 'g',  8: 'h',
        9: 'i',  10: 'j',
        11: 'k', 12: 'l',
        13: 'm', 14: 'n',
        15: 'o', 16: 'p',
        17: 'q', 18: 'r',
        19: 's', 20: 't',
        21: 'u', 22: 'v',
        23: 'w', 24: 'x',
        25: 'y', 26: 'z'
    }

def ReadFile():
    with open(r'Homework\5Seminar\input.txt', 'r') as data:
        for line in data:
            list = line.split()
        data.close

    text = list[0]
    return text

def Coder(input, dictionary, output):
    for i in range(1, len(dictionary), 1):
        n = input.count(dictionary[i])
        if(n == 0):
            break
        output = output + str(n) + dictionary[i]
    return output

def DeCoder(input, output):
    for i in range(0, len(input), 2):
        output = output + (int(input[i]) * input[i+1])
    return output


def WriteFile(output):
    print(output)
    with open(r'Homework\5Seminar\output.txt', 'w') as data:
        data.write(output)
        data.close

n = int(input("Выберите цифру \n 1 - закодировать \n 2 - декодировать \n>>> "))
if(n == 1):
    WriteFile(Coder(ReadFile(), dictionary, textOutput))
elif(n == 2):
    WriteFile(DeCoder(ReadFile(), textOutput))
else:
    while(n != 1 and n != 2):
        n = int(input("Выберите цифру \n 1 - закодировать \n 2 - декодировать \n>>> "))
    if(n == 1):
        WriteFile(Coder(ReadFile(), dictionary, textOutput))
    elif(n == 2):
        WriteFile(DeCoder(ReadFile(), textOutput))
