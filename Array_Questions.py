from collections import defaultdict
from math import pow

#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.
def single_one(nums):
    while len(nums) > 0:
        i = nums.pop(0)
        if i in nums:
            nums.remove(i)
        else:
            break
    return i

#Given an array, rotate the array to the right by k steps, where k is non-negative.
def rotate(nums,k):

    for i in range(k):
        removed = nums.pop()
        nums.insert(0, removed)
    return nums

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def containsDup(nums):
    dic = defaultdict(int)
    for i in nums:
        dic[i]+=1

    for v in dic.values():
        if v > 1:
            return True
    return False

def reverse_recur(s):
    if len(s) <= 1:
        return s

    return reverse_recur(s[1:]) + s[0]

def reverse_permutation(s):

    out =[]
    if len(s) ==1:
        out=[s]
    else:
        for i,let in enumerate(s):

            for perm in reverse_permutation(s[:i]+s[i+1:]):
                out +=[let+perm]
    return out

def fib_tabulation(n):

    table = [0]*(n+1)
    table[1] = 1
    for i in range(2,n+1):
        table[i] = table[i-2]+table[i-1]
    print(table)
    return table[n]


#Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
def intersect(nums1,nums2):

    ans = []
    for i in nums1:
        if i in nums2:
            nums2.remove(i)
            ans.append(i)
    return ans

#Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
def plusOne(digits):
    s = int("".join([str(i) for i in digits]))
    ans = s + 1
    return list(str(ans))

#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
def move_zeros(nums):
    idx=0
    for i in range(len(nums)):
        x = nums[i]
        if x != 0:
            nums[idx],nums[i] = nums[i],nums[idx]
            idx+=1
    return nums

def repeatedString(s, n):
    strlen = len(s)
    r, q = 0, 0
    q = n // strlen
    r = n % strlen

    acount = q * Counter(s, len(s)) + Counter(s, r)

    return acount


def Counter(s, length):
    count = 0
    for i in range(length):
        if s[i] == "a":
            count += 1
    return count


def Palindrome(s): #aaaa
    # w = ""
    # for i in s:
    #     w = i + w
    #
    # if (s == w):
    #     print("Yes")
    # else:
    #     print("No")
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return("No")
    return("Yes")


def Factorial(n):
    if n < 2:
        return 1
    return n*Factorial(n-1)

#check armstrong
def armstrong(n):
    order = len(str(n))
    print("order of the number is ",order)
    temp = n
    sum = 0
    while temp !=0:
        r = temp%10
        sum = sum + pow(r,order)
        temp = temp//10
    if sum == n:
        print("armstrong number")
    else:
        print("Not")

# Anagram Checker
def checkAnagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = defaultdict(int)
    for letter in s1:
        count[letter] += 1
    for letter in s2:
        count[letter] -= 1
    print(count)
    for k in count:
        if count[k] != 0:
            return "Not anagram"
    return "anagram"


def pair_target_sum(arr, target):
    ans = []
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        suma = arr[left] + arr[right]
        if suma == target:
            ans.append((arr[left], arr[right]))
        elif target > suma:
            left += 1
        else:
            right -= 1
        left += 1
        right -= 1
    if len(ans) >= 1:
        return ans
    else:
        return -1


def pair_target_sum2(arr, target):  # target = 4, arr=[1,3,2,2]
    seen = set()
    output = set()
    if len(arr) < 2:
        return

    for i in arr:
        k = target - i

        if k in seen:
            output.add((min(i, k), max(i, k)))
        else:
            seen.add(i)

    if len(output) >= 1:
        return " ".join(map(str, list(output)))
    else:
        return -1


def find_element(arr1, arr2):
    d = defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


def largestSum(arr):
    if len(arr) == 0:
        return 0
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum


def sentence_reversal(s):  # This is the best!
    words = []
    spaces = [" "]
    ans = []
    i = 0
    while i < len(s):
        if s[i] not in spaces:
            word_start = i
            while i < len(s) and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1

    for w in words[::-1]:
        ans.append(w)
    return " ".join(ans)

def compress(S):
    r = ""
    l = len(S)
    if l == 1:
        return S[0]+'1'

    i =1
    cnt =1
    while i< l:
        if S[i] == S[i-1]:
            cnt+=1
        else:
            r = r + S[i-1] +str(cnt)
            cnt=1
        i+=1
    r = r + S[i - 1] + str(cnt)
    return r


def find_duplicate(nums):
    num_set = set()
    ans = set()

    for i in range(len(nums)):

        if nums[i] in num_set:
            ans.add(nums[i])
        else:
            num_set.add(nums[i])
    if len(ans) == 0:
        return -1
    return ans


def unique(s):
    char = set()
    for let in s:
        if let in char:
            return False
        else:
            char.add(let)
    return True


def permutations(string, step=0):
    if step == len(string):
        print("".join(string))


    for i in range(step,len(string)):
        string_copy = [char for char in string]
        string_copy[step],string_copy[i] = string_copy[i],string[step]
        permutations(string_copy,step+1)

def balancecheck(s):
    if len(s) % 2 != 0:
        return False

    opening = set('([{')
    full = set([('(', ')'), ('[', ']'), ('{', '}')])
    print(full)

    stack = []
    for par in s:
        if par in opening:
            stack.append(par)
        else:
            if len(stack) == 0:
                return False

            last = stack.pop()

            if (last, par) not in full:
                return False

    return True


def LCP(X, Y):
    i = j = 0
    while i < len(X) and j < len(Y):
        if X[i] != Y[j]:
            break
        i = i + 1
        j = j + 1

    return X[:i]

def top_k_most_frequent(arr,k):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1
    print("dic",dic)
    l = []
    for w in sorted(dic,key=dic.get,reverse=True):
        print(w)
        l.append(w)

    return(l[:k])

def main():
    print("Single element is ", single_one([2,2,3,5,3,7,5,8]))
    print("move zeros", move_zeros([0,1,0,2,5]))
    # n = int(input("Enter number:"))
    # temp = n
    # rev = 0
    # while (n > 0):
    #     dig = n % 10
    #     rev = rev * 10 + dig
    #     n = n // 10
    # if (temp == rev):
    #     print("The number is a palindrome!")
    # else:
    #     print("The number isn't a palindrome!")

    a = [1, 1, 8, 2, 3, 4, 5, 5, 6, 7, 8]
    a.sort()
    for i in range(len(a) - 1, 0, -1):
        if a[i] == a[i - 1]:
            del a[i]
    print(a)
    print("largest sum : ",largestSum([1,4,-8,9]))
    print("Palindrome",Palindrome("aaa"))
    print("top k most frequent ",top_k_most_frequent([1,2,2,2,4,4],2))
    print("LCP",LCP("aaa","aaaa"))
    print("fac",Factorial(7))
    armstrong(120)
    print(checkAnagram('dog','god'))
    print(sentence_reversal("This is amazing!"))
    print("compressed",compress("AABBCC"))
    print(balancecheck('(('))
    print(reverse_recur("abcdef"))
    print(reverse_permutation("abc"))
    print(fib_tabulation(10))
main()
