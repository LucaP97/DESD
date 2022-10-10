def runHistogram():

    with open('histogram\grades.txt') as f:
        lines = f.read().splitlines()
    
    lines.sort(key = int)

    currMin = 1
    currMax = 10

    output = str(currMin) + " - " + str(currMax) + "\t\t|\t\t"

    for i in lines:
        if int(i) > currMax:
            currMin += 10
            currMax += 10
            output += "<br>" + str(currMin) + " - " + str(currMax) + "\t\t|\t\t"
        output += '*'
    
    print(output)
    return output