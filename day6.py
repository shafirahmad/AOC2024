with open("aoc2024/day6.txt", "r") as file:
    data = file.read().split("\n")

print(len(data), len(data[0]))

max = len(data)

row = 0
for line in data:
    col = line.find("^")
    if col >= 0:
        print(line, row, col)
        break
    row +=1

def printtable():
    for i in range(max):
        for j in range(max):
            if i == row and j == col:
                print("^>v<"[idir], end="")
            else:
                print(data[i][j], end="")
        print()
    print()


print(line, row, col)

orow,ocol = row,col

dir = [[-1,0], [0,1], [1,0], [0,-1]]
idir=0
visited = []
visited.append((row,col))
next = data[row][col]
while (row + dir[idir][0] >= 0 and 
       col + dir[idir][1] >= 0 and 
       col + dir[idir][1] < max and 
       row + dir[idir][0] < max):
    next = data[row+dir[idir][0]][col+dir[idir][1]]
    #print(row, col, idir, next)

    if next != "#":
        # continue
        visited.append((row+dir[idir][0],col+dir[idir][1]))
        row = row + dir[idir][0]
        col = col + dir[idir][1]
    else:
        #Collided
        idir= idir + 1
        if idir >= len(dir): 
            idir=0
        # We change direction but dont move

    #printtable()


print(visited)
print(len(visited))
print(len(set(visited)))

import time

possiblelocations = list(set(visited))
count = 0
for loc in possiblelocations:
    row,col = orow,ocol

    #print(">",loc,"<  ",end="", sep="")
    #start walking

    visited = {}
    idir=0
    while (row + dir[idir][0] >= 0 and 
        col + dir[idir][1] >= 0 and 
        col + dir[idir][1] < max and 
        row + dir[idir][0] < max):
        next = data[row+dir[idir][0]][col+dir[idir][1]]
        #print(row, col, idir, next)

        if next == "#" or (row+dir[idir][0] == loc[0] and col+dir[idir][1] == loc[1]):
            #Collided
            #print("#", end="")
            idir= idir + 1
            if idir >= len(dir): 
                idir=0
        else:
            # if location and direction are the same, then there is a loop
            if visited.get((row+dir[idir][0],col+dir[idir][1],idir),0):
                count +=1
                #print("*",end="")
                break
            visited[(row+dir[idir][0],col+dir[idir][1],idir)]=1
            row = row + dir[idir][0]
            col = col + dir[idir][1]
            #print(".", row,"-",col,sep="",end="")
    #end while
    #print()
    #time.sleep(.01)

print(count)

