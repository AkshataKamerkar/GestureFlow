def Bsearch(arr, a, b, key):

    mid = (a+b)//2
    # Base Condition
    if(key == arr[mid]):
        print("Key is present at : ", mid)
        exit()

    elif(key > arr[mid]):
        n = len(arr)
        Bsearch(arr, mid+1, n, key)
    elif(key < arr[mid]):
        b = mid
        Bsearch(arr, 0, b-1, key)
    else:
        print("Key not found")
        exit()

l = [20,30,40,50,60,70,80]

k = 10
print(Bsearch(l,0,len(l),k))

