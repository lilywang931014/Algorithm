def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=", ")
    print()

if __name__ == "__main__":

    myList = [12,11,13,5,7,6]
    print("Unsorted List is ", end="\n")
    printList(myList)
    bubble_sort(myList)
    print("Sorted List is ", end="\n")
    printList(myList)
