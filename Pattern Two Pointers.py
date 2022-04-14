import math
from collections import defaultdict

#Target Sum. Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
def target_sum(arr,target):
    arr.sort()
    left,right = 0, len(arr)-1
    sum = 0

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return [left,right]

        elif sum > target:
            right -=1
        else:
            left+=1
    return [-1,-1]


# Remove Duplicate from list without using extra space
def remove_duplicate(arr): #12234

    i = 1
    next_non_duplicate = 1

    while i < len(arr):
        if arr[next_non_duplicate -1 ] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            print(arr)
            next_non_duplicate+=1
        i+=1
    return next_non_duplicate


#Remove key from list and give new length
def remove_key(arr,key): #[1,2,3,4,4,5,5],4
    non_key = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[non_key] = arr[i]
            non_key+=1
    print("yo",arr)
    return non_key

#Square a Sorted array and put it in another array
def square(arr):

    n = len(arr)
    squares = [0]*n
    highest = n-1
    left,right = 0,n-1

    while left <= right:
        leftSquare = arr[left]**2
        rightSquare = arr[right]**2

        if leftSquare > rightSquare:
            squares[highest] = leftSquare
            left+=1
        else:
            squares[highest] = rightSquare
            right-=1

        highest -=1
    return squares

def triplets(arr): #[-3,-2,-1,0,1,1,2]
    arr.sort()
    triplet=[]
    for i in range(len(arr)):
        if i >0 and arr[i-1] == arr[i]:
            continue
        searchPair(arr,-arr[i],i+1,triplet)
    return triplet

def searchPair(arr,target,left,triplet):
    right = len(arr) - 1
    current_sum = 0
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            triplet.append([-target,arr[left],arr[right]])
            left+=1
            right -=1
            while left < right and arr[left] == arr[left-1]:
                left +=1
            while left < right and arr[right] == arr[right +1]:
                right -=1

        elif current_sum > target :
            right -=1
        else:
            left +=1

#Unique number triplets with sum smaller than target
def smallerTriplets(arr,target): #1111 5
    arr.sort()
    triplets=[]
    for i in range(len(arr)-2):
        findSum(arr,target-arr[i],i,triplets)
    return triplets

def findSum(arr,target_sum,first,triplets):
    count = 0
    left,right = first+1,len(arr)-1
    while left < right:
        if arr[left] + arr[right] < target_sum :
            for i in range(right,left,-1):
                if arr[left] != arr[i] and arr[i] != arr[first] and arr[left] != arr[first]:
                    triplets.append([arr[first],arr[left],arr[i]])
            left+=1
        else:
            right -=1
    return count

#Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects,
# hence, we can’t count 0s, 1s, and 2s to recreate the array.
def Dutch_flag_sort(arr): #[0,1,2,0,1,2] -> [0,0,1,1,2,2]

    low,high = 0,len(arr)-1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i],arr[low] = arr[low],arr[i]
            low+=1
            i+=1
        elif arr[i] == 1:
            i+=1
        else:
            arr[high],arr[i]= arr[i],arr[high]
            high-=1

def quadraplets(arr,target):
    arr.sort()
    quad = []
    for i in range(len(arr)-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1,len(arr)-2):
            if j > 0 and arr[j] == arr[j - 1]:
                continue
            findTarget(arr,target,i,j,quad)
    return quad

def findTarget(arr,target,first,second,quad):

    left = second +1
    right = len(arr)-1

    arr_sum = 0

    while (left < right):
        arr_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if arr_sum == target :
            quad.append([arr[first], arr[second] ,arr[left] ,arr[right]])
            left+=1
            right-=1
            while left < right and arr[left] == arr[left-1]:
                left+=1
            while left < right and arr[right] == arr[right + 1]:
                right -=1
        elif arr_sum > target:
            right-=1
        else:
            left+=1

def minimumAbsDifference(arr):
        arr.sort()
        dic = defaultdict(list)
        print("yo",list((zip(arr,arr[1:]))))

        for a,b  in zip(arr, arr[1:]):
            dic[b-a].append([a,b])
        print(dic)
        val = min(dic.keys())
        return dic[val]

#Minimum Window Sort- Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
def shortest_window_sort(arr): #1,2,-3,0,1,7,10
    low,high = 0,len(arr)-1
    while(low < len(arr)-1 and arr[low] <= arr[low+1]):
        low+=1 #1

    if low == len(arr)-1:
        return 0

    while(high > 0 and arr[high] >= arr[high-1]):
        high -=1 #2

    subarray_maximum,subarray_minimum = -math.inf,math.inf
    for k in range(low,high+1):
        subarray_maximum = max(subarray_maximum,arr[k])
        subarray_minimum = min(subarray_minimum,arr[k])

    while(low > 0 and arr[low-1] > subarray_minimum):
        low -=1
    while(high < len(arr)-1 and arr[high+1] < subarray_maximum):
        high+=1
    return high-low+1

#program to find largest pair sum in a given array
def largest_pair_sum(arr): #[1,4,3,10,2]
    if len(arr) < 2:
        return -1

    if arr[0] > arr[1]:
        higher = arr[0]
        lower = arr[1]

    higher = arr[1]
    lower = arr[0]

    for i in range(2,len(arr)):
        if arr[i] > higher:
            lower = higher
            higher = arr[i]

        elif arr[i] > lower and arr[i] != higher:
            lower = arr[i]
    print(higher,lower)
    return higher + lower


def main():
    print("target sum", target_sum([1,2,3,4], 5))
    print("Remove Duplicate", remove_duplicate([2, 3, 3, 3, 6, 9, 9]))
    print("length after removing key", remove_key([1,2,3,4,4,5,5],4))
    print("Squared Array", square([-2, -1, 0, 2, 3]))
    print("Triplets to 0", triplets([-3,-3,-3,2,1,-1,2,3,4,-4,0]))
    print("Smaller Triplets", smallerTriplets([-1, 0, 2, 3, -1], 3))
    array = [0,1,2,0,1,2]
    Dutch_flag_sort(array)
    print(array)
    print("Quad",quadraplets([4,1,2,-1,1,-3,6,0],6)) #[-3,-1,0,1,1,2,4,5,6]
    print("shortest subaaray needed to be sorted",shortest_window_sort([1,2,-3,0,1,7,10]))
    print("min",minimumAbsDifference([1,2,3,4,9]))
    print("largest pair sum : ", largest_pair_sum([1,4,9,10,2]))
main()
