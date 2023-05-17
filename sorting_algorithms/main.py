import random

numList = []
for i in range(1, 20):
    numList.append(random.randrange(1, 100))


def insertion_sort():
    for i in range(len(numList)):
        for j in range(i, 0, -1):
            if (numList[j-1] > numList[j]):
                numList[j-1], numList[j] = numList[j], numList[j-1]
                continue

    print(numList)

def bubble_sort():
    swapped = True
    while (swapped):
        swapped = False
        for i in range(len(numList) - 1):
            nextElement = i + 1
            if i == len(numList) - 1:
                continue

            if (numList[i] > numList[nextElement]):
                numList[nextElement], numList[i] = numList[i], numList[nextElement]
                swapped = True
    
    print(numList)

insertion_sort()