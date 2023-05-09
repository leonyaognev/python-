ass = input()
ass = ass.split(' ')
ss = int(ass[0])
for i in range(int(ass[1])):
    if ss[-1] == 0:
        ss.rstrip(0)
    ss = int(ass) - 1