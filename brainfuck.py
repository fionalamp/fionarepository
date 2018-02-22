# fionarepository
programming beginnings
foula = 0
signal = 0
tape = [0] * 10000
bfcode = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
def getLoops(bfcode):
    tralha = []

    fiona = {}

    for i, c in enumerate(bfcode):
        if c == '[':
            tralha.append(i)

        if c == ']':
            temp = tralha.pop()

            fiona[temp] = i
            fiona[i] = temp

    return fiona


loops = getLoops(bfcode)

result = ''

tp = 0

while signal < len(bfcode):
    comando = bfcode[signal]
    if comando == '+':
        tape[foula] += 1
        signal += 1
    elif comando == '-':
        tape[foula] -= 1
        signal += 1
    elif comando == '.':
        result += chr(tape[foula])
        signal += 1
    elif comando == '>':
        foula += 1
        signal += 1
    elif comando == '<':
        foula -= 1
        signal += 1
    elif comando == '[':
        if tape[foula] > 0:
            signal += 1
        else:
            signal = loops[signal] + 1
    elif comando == ']':
        if tape[foula] > 0:
            signal = loops[signal]
        else:
            signal += 1
    else:
        signal += 1

print (result)
