

def insertation_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if(lst[j-1] > lst[j]):
                    temp = lst[j-1]
                    lst[j-1] = lst[j]
                    lst[j] = temp
    return lst


lst = [3,7,4,9,5,2,6,1]
print(insertation_sort(lst))
print lst


