with open("aoc2024/day7.txt", "r") as file:
    data = file.read().split("\n")

#print(len(data), len(data[0]))

max = len(data)

operations = ["+", "*"]

def mycalc(ss,dd,zz,idx):
    #print(" "*10*idx, "(",idx,")", ss, zz, end=" ")
    if idx < len(dd)-1:
        z = zz + dd[idx+1]
        #print(zz," +", dd[idx+1], "=", z)
        if mycalc(ss,dd,z,idx+1):
            return True
        z = zz * dd[idx+1]
        #print(zz," *", dd[idx+1], "=", z)
        if mycalc(ss,dd,z,idx+1):
            return True
    else:
        if zz == ss:
            #print(" True1")
            return True
    return False

def mycalc2(ss,dd,zz,idx):
#    print(" "*10*idx, "(",idx,")", ss, zz, end=" ")
    if idx < len(dd)-1:
        z = zz + dd[idx+1]
#        print(zz," +", dd[idx+1], "=", z)
        if mycalc2(ss,dd,z,idx+1):
            return True
        z = zz * dd[idx+1]
#        print(zz," *", dd[idx+1], "=", z)
        if mycalc2(ss,dd,z,idx+1):
            return True
        z = int( str(zz) + str(dd[idx+1]) )
#        print(zz," ||", dd[idx+1], "=", z)
        if mycalc2(ss,dd,z,idx+1):
            return True
    else:
        if zz == ss:
            #print(" True2")
            return True
    return False


part1 = 0
part2 = 0
for line in data:
    ss, dd = line.split(": ")
    ss = int(ss)
    dd = dd.split(" ")
    dd = [int(x) for x in dd]
    #print("Row",ss, dd)

    val =  mycalc(ss,dd,dd[0],0)
    if val:
        part1 += ss
        part2 += ss
    else:
        val =  mycalc2(ss,dd,dd[0],0)
        if val:
            part2 += ss


print("Result", part1, part2)
