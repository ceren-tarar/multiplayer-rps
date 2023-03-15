# -*- coding: utf-8 -*-

def rps(o1,o2):
    dif = abs(o1-o2)
    if dif==1:
        if o1>o2:
            result="win"
        else:
            result = "lose"
    elif dif==2:
        if o1<o2:
            result="win"
        else:
            result ="lose"
    else:
        result = "tie"

    return result

print('Enter number of players:')
ps = input()
ps = int(ps)

arr = [0]*ps

print("Select from [r,p,s]")
for i in range(ps):
    print(f'Player {i+1}:')
    select = input()
    if select == "r":
        s = 0
    elif select == "p":
        s = 1
    elif select == "s":
        s = 2
    else:
        print("Invalid selection")
    arr[i] = [i,s,0]


for i in range(len(arr)):
    for c in range(1,len(arr)):
        print(c)

        try:
            res = rps(int(arr[i][1]),int(arr[i+c][1]))
 
            if res == "win":
                arr[i][2]+=1

            elif res == "lose":
                arr[i+c][2]+=1
        except:
            print()

scorelist = [0]*ps
for i in range(len(arr)):
    scorelist[i] = arr[i][2]

indices = [index for index, item in enumerate(scorelist) if item == max(scorelist)]


if len(indices) == 1:
    print(f'Winner is Player {indices[0]+1}!!')
else:
    for i in range(len(indices)):
        indices[i]=indices[i]+1
        
    print(f'Tie between players: {indices} ')
