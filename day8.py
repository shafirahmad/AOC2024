import time
start = time.time()
print("Time",time.time()-start)
with open("aoc2024/day8.txt", "r") as file:
    data = file.read().split("\n")

print(len(data), len(data[0]))

max = len(data)

locs = {}
for rno in range(len(data)):
    for cno in range(len(data[rno])):
        c = data[rno][cno]
        if c != ".":
            if locs.get(c,".") == ".":
                locs[c] = [(rno,cno)]
            else:
                locs[c].append((rno,cno))

print("Time",time.time()-start)

antinodes = {}
for c in locs.keys():
    #print(c,locs[c])
    d = locs[c]
    for i in range(len(d)-1):
        for j in range(i+1, len(d)):
            x1,y1 = d[i][0], d[i][1]
            x2,y2 = d[j][0], d[j][1]
            #print(x1,y1,x2,y2)
            #Find possible antinodes
            nx = x1-(x2-x1)
            ny = y1-(y2-y1)
            if (nx>=0 and nx<max) and (ny>=0 and ny<max):
                antinodes[(nx,ny)]=1

            nx = x2+(x2-x1)
            ny = y2+(y2-y1)
            if (nx>=0 and nx<max) and (ny>=0 and ny<max):
                antinodes[(nx,ny)]=1

            #print(antinodes)
print("Part1",len(antinodes))

print("Time",time.time()-start)

antinodes = {}
for c in locs.keys():
    d = locs[c]
    for i in range(len(d)-1):
        for j in range(i+1, len(d)):
            for k in range(0,51):
                x1,y1 = d[i][0], d[i][1]
                x2,y2 = d[j][0], d[j][1]
                #print(x1,y1,x2,y2)
                #Find possible antinodes
                nx = x1-(x2-x1)*k
                ny = y1-(y2-y1)*k
                if (nx>=0 and nx<max) and (ny>=0 and ny<max):
                    antinodes[(nx,ny)]=1

                nx = x2+(x2-x1)*k
                ny = y2+(y2-y1)*k
                if (nx>=0 and nx<max) and (ny>=0 and ny<max):
                    antinodes[(nx,ny)]=1

                #print(antinodes)
print("Part2",len(antinodes))
print("Time",time.time()-start)
