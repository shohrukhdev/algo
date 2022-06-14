
def selSort(array):
    unsorted = array.copy()
    for i in range(len(array)):
        minInd = i
        for j in range(i+1, len(array)):
            if array[minInd] > array[j]:
                minInd = j

        array[i], array[minInd] = array[minInd], array[i]

    print("Array: " + str(unsorted) + "\nSorted array: " + str(array))

if __name__ == '__main__':
    selSort([5, 2, 5, 7, 0, 8])
