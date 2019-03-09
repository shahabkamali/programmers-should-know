

def selection_sort(lst):
    for i in range(0, len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        temp = lst[min_index]
        lst[min_index] = lst[i]
        lst[i] = temp

    return lst

lst = [5,10,15,1,8]

print(selection_sort(lst))

