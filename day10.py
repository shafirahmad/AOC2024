import time
start = time.time()
print("Time",time.time()-start)
with open("aoc2024/day10.txt", "r") as file:
    data = file.read().split("\n")

print(len(data), len(data[0]))

mm = []
for row in data:
    mm.append( [int(x) if x != "." else -1 for x in row] )

max = len(mm)


dir = [[0,1],[1,0],[-1,0],[0,-1]]

def countroutes(x,y,num):
    numroutes=0
    if num == 9:
        if (x >=0 and x <max and y >=0 and y < max):
            score.append((x,y))
            return 1
        return 0
    for d in dir:
        if (x+d[0] >=0 and x+d[0] <max and y+d[1] >=0 and y+d[1] < max):
            if mm[x+d[0]][y+d[1]] == num+1:
                numroutes += countroutes(x+d[0],y+d[1],num+1)
    return numroutes

ss = 0
su = 0
sq = 0
for i in range(max):
    for j in range(max):
        if mm[i][j] == 0:
            #print("*"*40)
            score = []
            ss += countroutes(i,j,0)
            sq += len(score)
            #print(score, len(score), len(set(score)))
            su += len(set(score))

print(ss)
print(su)
print(sq)

print("Time",time.time()-start)

exit(0)
