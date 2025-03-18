with open("aoc2024/day5.txt", "r") as file:
    rules,seqx = file.read().split("\n\n")

rules = rules.split("\n")
print("rules", len(rules))

seqx = seqx.split("\n")
print("seqx", len(seqx))

myrules = {}
for rule in rules:
    a,b = rule.split("|")
    myrules[a+"-"+b]= a
    myrules[b+"-"+a]= a

print(myrules)

mysum = 0
failedseqx = []
for seq in seqx:
    myseq = seq.split(",")
    #print(len(myseq), myseq)
    numseq = len(myseq)
    valid = True
    for i in range(numseq-1):
        for j in range(i+1, numseq):
            #print(i,j, myseq[i],myseq[j], "==", myrules[str(myseq[i])+"-"+str(myseq[j])])
            if myseq[i] != myrules[str(myseq[i])+"-"+str(myseq[j])]:
                #print("not")
                valid = False
                break
    #print(seq, valid)
    if valid:
        mysum+= int(myseq[int((numseq-1)/2)])
        #print(mysum, int(myseq[int((numseq-1)/2)]))
    else:
        failedseqx.append(myseq)
    #print()

print(mysum)

# Now have all the failed seq in failedseqx, how to sort them?

mysum2=0
for myseq in failedseqx:
    print(myseq, end=" ")
    numseq = len(myseq)
    for i in range(numseq-1):
        swapped = False
        for j in range(numseq-1):
            if myseq[j] != myrules[str(myseq[j])+"-"+str(myseq[j+1])]:
                # Wrong order, lets swap them
                swapped = True
                myseq[j], myseq[j+1] = myseq[j+1], myseq[j]
        if not swapped:
            break;
    #end for i
    mysum2+= int(myseq[int((numseq-1)/2)])
    print(myseq, mysum2)

print(mysum2)