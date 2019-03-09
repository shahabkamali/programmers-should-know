def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp



def bubble_sort2(alist):
    for i in range(0, len(alist)-1):
        for j in range(0, len(alist) - i - 1):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


alist = [54,26,93,17,77,31,44,55,20]
bubble_sort2(alist)
print(alist)
