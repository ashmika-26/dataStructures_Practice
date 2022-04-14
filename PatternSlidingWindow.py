import math
from collections import defaultdict

#Maximum Sum Subarray of Size K (easy)
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

def max_subarray_k(arr, k): #[1,2,3,4,5]

    max_sum=0
    window_start=0
    window_sum = 0

    for window_end in range(len(arr)): #window_end goes till the end of the list
        window_sum += arr[window_end] #Add the next elements
        if window_end >= k-1: #stop adding elements if k value is reached
            max_sum = max(max_sum,window_sum) #Once k value is reached find the maximum sum
            window_sum -= arr[window_start] #Now subtract the starting element from the sliding window so that we can add the next element and check again.
            window_start +=1 #increase the starting element
    return max_sum


#Smallest Subarray with a given sum (easy)
# Given an array of positive numbers and a positive number ‘S’,
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
def smallest_subarray_w_given_sum(arr,S): #12345 , 3

    min_length = math.inf
    window_start = 0
    window_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end] #We add the elements in the list till the end.

        while window_sum >= S: #We enter this loop once the window_sum becomes more than or equal to the given sum.
            min_length = min(min_length,window_end - window_start + 1)  # find the minimum length by finding the length of the subarray done by subtracting end and stqrt +1
            window_sum-= arr[window_start] #subtract the first element from the window sum
            window_start+=1 #Now just increase the starting value

    if min_length == math.inf:
        return 0

    return min_length


# Longest Substring with K Distinct Characters (medium)
def longest_substring_with_k_distinct(str,k): #aaabbc dic { b:2 c:1 a:1

    max_length = 0
    start = 0
    dict = defaultdict(int)

    #Add elements till the end of the list
    for end in range(len(str)):
        right = str[end]
        dict[right] +=1

        while len(dict) > k: #We only enter this loop once there are more than k distinct characters in the dictionary
            left = str[start]
            dict[left]-=1
            if dict[left] == 0:
                del dict[left] #We are basically deleteing the characters from dictionary so we can add them again in future and also check number of dictinct chars.
            start+=1

        max_length = max(max_length,end-start+1) #We check this at every step
    return max_length


#Fruits into Baskets (medium)
def max_fruits_in_basket(arr):
    max_length = 0
    start = 0
    dic = defaultdict(int)

    for end in range(len(arr)):
        right_char = arr[end]
        dic[right_char] += 1
        while len(dic) > 2:
            left_char = arr[start]
            dic[left_char] -= 1
            if dic[left_char] == 0:
                del dic[left_char]
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length

#No-repeat Substring (hard)
# Given a string, find the length of the longest substring which has no repeating characters.
def non_repeat_substring(str): #[aabcabb]

    window_start = 0
    max_length = 0
    dict = defaultdict(int)

    for end in range(len(str)):
        if str[end] in dict: #3. After that we start checking
            window_start = max(window_start,dict[str[end]]+1) #If the character is already in dict, then we just make the start value as the one after the repeating character index
        dict[str[end]] = end #1. First we come here and add the first char to dictionary as their index
        max_length = max(max_length,end-window_start+1) #2. then we just keep seeing the maximum length
    return max_length

#Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
# find the length of the longest substring having the same letters after replacement.
def length_longest_substring(str,k): # aaabbc 2
    max_length, window_start,max_rep = 0,0,0
    dict = defaultdict(int)
    for end in range(len(str)):
        dict[str[end]] +=1 #First we just keep a dictionary of the number of characters in str
        max_rep = max(max_rep,dict[str[end]]) #maximum repeating character is repeated how many times

        if (end-window_start+1 - max_rep) > k: #if maximum number that can be replaced is greater than k
            if max_rep == dict[str[window_start]]:
                max_rep -=1
            dict[str[window_start]] -=1 #then remove the first character from dic
            window_start +=1 #a new start
            print("mr",max_rep)

        max_length =  max(max_length,end-window_start+1)
        #print(max_length)
    return max_length

#MAximum repeating Ones in an array of 1s and 0s
def length_longest_OnesArray(arr,k): #[0,1,1,0,0,0,1,1,0,1,1] , 2
    max_length, window_start, max_Ones = 0, 0, 0

    for end in range(len(arr)):
        if arr[end] == 1:
            max_Ones+=1

        if (end-window_start +1 - max_Ones) > k:
            if arr[window_start] == 1:
                max_Ones-=1
            window_start+=1

        max_length = max(max_length,end-window_start+1)
    return max_length


#Permutation in a String (hard)
def find_permutation(str,pattern): # ab eiaobbaooo
    window_start, matched = 0,0
    pattern_dict = defaultdict(int)
    for i in pattern: #First we just add the pattern in a dictionary
        pattern_dict[i]+=1 #a:1 b:1

    for end in range(len(str)): # 0
        if str[end] in pattern_dict:
            pattern_dict[str[end]] -=1 # if the char is in dict, the  we subtract 1 from its value
            if pattern_dict[str[end]] == 0: #if that particular char becomes 0 increase matched
                matched+=1 #matched = 0

        if matched == len(pattern_dict): #If we found matched = length of the pattern the we have our answer
            return True

        if end >= len(pattern)-1 :  #when the string becomes = or greater than the pattern length.
            if str[window_start] in pattern_dict: #Only enter here if the starting char is in pattern
                if pattern_dict[str[window_start]] == 0:
                    matched -=1
                pattern_dict[str[window_start]] +=1 #We add it back to the pattern since we didn't find matched pattern yet
            window_start +=1 # 1

    return False

#Smallest Window containing Substring (hard)
# #Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
def smallest_window_containing_substring(str,pattern): #ababdec abc
    start,matched,start_substring = 0,0,0
    dict = defaultdict(int)
    min_length = len(str) + 1

    for i in pattern: #a:0 b:0 c:0
        dict[i] +=1

    for end in range(len(str)): #
        right = str[end]
        if right in dict:
            dict[right]-=1
            if dict[right] >= 0:
                matched+=1 #matched = 2x

        while matched == len(pattern): #3
            if min_length > end-start+1:
                min_length = end-start+1
                start_substring = start
            left = str[start]
            if left in dict:
                if dict[left] == 0:
                    matched -= 1
                dict[left] += 1
            start += 1

    if min_length > len(str):
        return ""
    return str[start_substring:start_substring+min_length]


def main():
    print(max_subarray_k([1,2,3,4,5],2))
    print(smallest_subarray_w_given_sum([1,2,3,4],6))
    print("ans",longest_substring_with_k_distinct("aaabbc",2))
    print(non_repeat_substring("aabccbb"))
    print(length_longest_substring("abbaacbbabb",2))
    print(length_longest_OnesArray([0,1,1,0,0,0,1,1,0,1,1] ,2))
    print(find_permutation("abcdxabcde","abcdeabcdx"))
    print(smallest_window_containing_substring("ababdec","abc"))


main()