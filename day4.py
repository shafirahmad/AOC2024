with open("aoc2024/day4.txt", "r") as file:
    lines = file.read().split("\n")
    print(len(lines), len(lines[0]))

z = len(lines)

strtofind = "XMAS"
directions = [[1,0], [0,1], [0,-1], [-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

data=[]
data.append(" "*(z+6))
data.append(" "*(z+6))
data.append(" "*(z+6))
for line in lines:
    data.append("   "+line+"   ")
data.append(" "*(z+6))
data.append(" "*(z+6))
data.append(" "*(z+6))

print(len(data), len(data[0]))

count=0
for x in range(3,z+3):
    for y in range(3,z+3):
        for direction in directions:
            found=True
            #direction = directions[i]
            for j in range(len(strtofind)):
                #print(x+j*direction[0],y+j*direction[1])
                if data[x+j*direction[0]][y+j*direction[1]] != strtofind[j]:
                    found=False
                    break
            if found:
                count +=1
    print(x,count)

print(count)

str2 = "MASMS"
str2dir =[[0,0], [1,1],[2,2],[2,0],[0,2]]
str2dir2 =[[0,0], [1,1],[2,2],[0,2],[2,0]]
#str2dir2 =[[0,0], [1,-1],[2,-2],[2,0],[0,-2]]

count=0
for x in range(3,z+3):
#for x in [4]:
    for y in range(3,z+3):
        for direction in directions[4:]:
            found=True
            #print("reset T")
            for j in range(len(str2)):
                # print(x, y, direction, j, str2dir[j], (str2dir[j][0])*direction[0], (str2dir[j][1])*direction[1],
                #       x+(str2dir[j][0])*direction[0],
                #       y+(str2dir[j][1])*direction[1],
                #       data[x+(str2dir[j][0])*direction[0]][y+(str2dir[j][1])*direction[1]],
                #       str2[j] )
                if data[x+(str2dir[j][0])*direction[0]][y+(str2dir[j][1])*direction[1]] != str2[j]:
                    found=False
                    #print("reset F")
                    #break
            if found:
                # print("found")
                count +=1
            found=True
            # print("reset T")
            for j in range(len(str2)):
                # print(x, y, direction, j, str2dir[j], (str2dir[j][0])*direction[0], (str2dir[j][1])*direction[1],
                #       x+(str2dir2[j][0])*direction[0],
                #       y+(str2dir2[j][1])*direction[1],
                #       data[x+(str2dir2[j][0])*direction[0]][y+(str2dir2[j][1])*direction[1]],
                #       str2[j] )
                if data[x+(str2dir2[j][0])*direction[0]][y+(str2dir2[j][1])*direction[1]] != str2[j]:
                    found=False
                    # print("reset F")
                    #break
            if found:
                # print("found")
                count +=1
    print(x,count,count/2)




