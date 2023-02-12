def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list1[mid] < n:
            low = mid + 1
        elif list1[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1
def inputted():
    list1=[]
    y = 3
    print("Please enter 3 numbers either of which should be 45.")
    for i in range(0, y):
        ele = int(input())
        list1.append(ele)
    print(list1)
    n=45;
    result = binary_search(list1, n)
    if result!=-1:
        print("VERIFIED")
        from PyDictionary import PyDictionary
        ch=str(input("What would you like to access today? :  a) meaning b)synonym c)antonym"))
        if(ch=='a'):
            dict = PyDictionary()
            word=input("Please enter word whose meaning is to be found:")
            mean = dict.meaning(word)
            print(mean)
        elif(ch=='b'):
            dict=PyDictionary()
            word=input("Please enter worrd whose synonym is to be found: ")
            syn= dict.synonym(word)
            print(syn)
        elif(ch=='c'):
            dict=PyDictionary
            word=input("Please enter word whose antonym is to be found: ")
            ant=dict.antonym(word)
            print(ant)
    else:
        print("SORRY TRY AGAIN LATER!")

inputted()

