list1 = [12, 18, 2, 6, 3]


def sort(start, end):
    pivot = list1[len(list1)-1]
    running = True
    itemFromLeft=0
    itemFromRight=0
    mid = (end-start) // 2 + start

    while running:
        if end == start:
            return
        for i in range(start, end):
            if list1[i] > pivot:
                itemFromLeft = i
                break
        
        for j in range(end, start-1,-1):
            if list1[j] < pivot:
                itemFromRight = j
                break

            
        if itemFromLeft < itemFromRight:
            temp = list1[itemFromRight]
            list1[itemFromRight]=list1[itemFromLeft]
            list1[itemFromLeft]=temp
        else:
            temp = list1[itemFromLeft]
            list1[itemFromLeft] = list1[end]
            list1[end] = temp
            print(list1)
            running = False
            
            sort(start, mid - 1)
            sort(mid + 1, end)
        
    
    
        

sort(0, 4)