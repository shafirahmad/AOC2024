import time
start = time.time()
print("Time",time.time()-start)
with open("aoc2024/day9.txt", "r") as file:
    data = file.read().split("\n")

print(len(data), len(data[0]))

data = data[0]
max = len(data)

i=0
ss = 0
fs = [-1]*95088
fp = 0

files = {}
gaps={}
fileid=0
gapid=0
while i < max:
    val = int(data[i])
    if i % 2:
        #freespace
        #print("Space", data[i])
        gaps[gapid] = [fp,val]
        for j in range(val):
            fs[fp] = -1
            fp +=1
        gapid+=1
    else:
        # File
        #print("File", fileid, data[i])
        files[fileid] = [fp,val]
        for j in range(val):
            fs[fp] = fileid
            fp +=1
        fileid = fileid + 1

    ss += val
    i+=1
#end while

fs2 = fs.copy()

print(i,ss)
print("Time",time.time()-start)

fp = 0
ep = len(fs)-1

print("fpep",fp,ep)
while fp+2 < ep:
    while fs[ep] == -1:
        ep -= 1
    # We have a valid ep
    while fs[fp] != -1:
        fp += 1
    # We have a blank fp
    # Swap fp and ep
    fs[fp], fs[ep] = fs[ep], fs[fp]
    # print((fp,ep),end=" ")

#Calculate score

ss = 0
for i in range(len(fs)):
    if fs[i] == -1:
        pass
    else:
        ss += fs[i] * i
print(fp,ep)
print(ss)
print(fs[fp-5:fp+20])
for i in range(fp-5,fp+5):
    print(i,fs[i])


print(6344673860001 - 5201*50126 + 5201*50125) # Off by one error!!!!!
print("Time",time.time()-start)
# Part2
# use fs2 as the filesystem, and files and gaps

print("Gaps", gaps[0], gaps[1], gaps[2])
print("Files", files[0], files[1], files[2])

def findgaps(fs):
    ingap=False
    gaplen = 0
    gapno = 0
    gaps={}
    for i in range(len(fs)):
        if fs[i] == -1:
            #ingap
            ingap=True
            gaplen+=1
            gaps[gapno] = [i-gaplen+1,gaplen]
        else:
            if ingap:
                gaplen=0
                ingap=False
                gapno+=1
    #del gaps[gapno]
    return gaps
found=True
for fileid in range(len(files)-1,1,-1):
    filepos, filelen = files[fileid]
    #print(fileid,filepos,filelen)
    if found:
        gaps = findgaps(fs2)
        found=False
    for i in range(len(gaps)):
        gappos, gaplen = gaps[i]
        if gaplen >=filelen and filepos > gappos: #and gaplen <=9
            files[fileid] = [gappos,-1]
            for j in range(filelen):
                fs2[gappos] = fileid
                fs2[filepos] = -1
                gappos  += 1
                filepos += 1
            found=True
            break
            #end j
        #endif
    #end i
    #print("+", end="")
#end for


ss = 0
for i in range(len(fs2)):
    if fs2[i] == -1:
        pass
    else:
        ss += fs2[i] * i
print("Part2", ss)

#print(6344673860001 - 5201*50126 + 5201*50125) # Off by one error!!!!!
print("Time",time.time()-start)
# Part2
# use fs2 as the filesystem, and files and gaps

# print("Gaps", gaps[0], gaps[1], gaps[2])
# print("Files", files[0], files[1], files[2])






print("Time",time.time()-start)
exit(0)