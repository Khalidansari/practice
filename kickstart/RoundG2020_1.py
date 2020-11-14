T = int(input())

for i in range(T):
    inputStr = input()

    count = 0
    numberOfKicks = 0

    for x in range(len(inputStr) - 4):
        if (inputStr[x] == "K" and inputStr[x+1] == "I" and inputStr[x+2] == "C" and inputStr[x+3] == "K"):
            numberOfKicks = numberOfKicks + 1
        elif (inputStr[x] == "S" and inputStr[x+1] == "T" and inputStr[x+2] == "A" and inputStr[x+3] == "R" and inputStr[x+4] == "T"):
            count = count + numberOfKicks
    print("Case #" + str(i+1) + ": " + str(count))