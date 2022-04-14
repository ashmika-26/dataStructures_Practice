#Selection Sort Time Complexity O(n)

def sequential(arr,ele):

    Found = False
    i = 0

    while i < len(arr) and not Found:
        if arr[i] == ele:
            Found = True
        else:
            i+=1
    return Found

def order_sequential(arr,ele):
    Found = False
    Stopped = False
    i= 0
    while i < len(arr) and not Found and not Stopped:
        if arr[i] == ele:
            Found = True
        else:
            if arr[i] > ele:
                Stopped = True
            else:
                i+=1
    return Found
# Binary Search Time complexity O(logn)
def iterbinary(arr,ele):
    first = 0
    last = len(arr)-1
    Found = False
    while first <= last and not Found:
        mid = (first+last)//2
        if arr[mid] == ele:
            Found = True
        elif ele > arr[mid]:
            first = mid+1
        else:
            last = mid -1
    return Found

def recbinary(arr,ele):

    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2

        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return recbinary(arr[:mid],ele)
            else:
                return recbinary(arr[mid+1:],ele)

def find_first_occurence(arr,k): #[1,4,4,5,5,6], 4
    low,high = 0,len(arr)-1
    result = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == k:
            result = mid
            print(result)
            high = mid-1
        elif k> arr[mid]:
            low = low+1
        else:
            high = mid -1
    return result

def find_element_equal_to_index(arr): #[1,3,6,]
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high+low)//2
        print("low,high", low, high)
        print("midm",mid)
        diff = arr[mid] - mid
        print('diff',diff)
        if diff == 0:
            return mid
        elif diff > 0:
            high = mid -1
        else:
            low = mid+1
        print("low,high", low, high)

def main():

    print(order_sequential([1,2,9,70,566],70))
    print(sequential([5,3,10,1,2],1))
    print(iterbinary([1,2,3,5,8],80))
    print(recbinary([1,2,3,5,8],8))
    print(find_element_equal_to_index([2,2,6,7,4]))


main()