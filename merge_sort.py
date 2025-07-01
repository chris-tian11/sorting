list1 = [3, 6, 9 , 15]
list2 = [2, 12, 16 , 18]





for i in range(4):
    if list1[0] > list2[0]:
        if list2[1] > list2[2]:
            removed_num = list1[1]
            list1.pop(1)
            list2.insert(2, removed_num)
            print(list1)
            print(list2)
        
        else:
            removed_num = list1[0]
            list1.pop(0)
            list2.insert(1, removed_num)
            print(list1)
            print(list2)
    elif list1[0] < list2[0]:
        removed_num = list1[0]
        list1.pop(0)
        list2.insert(0, removed_num)
        print(list1)
        print(list2)