# a = list((1, 2, 3, 'apple', 4.5))
# print(a)
# b = list("GFG")
# print(b)
import bisect
# a = [2, 4, 6, 8, 10]
#
# # Linear search using 'in'
# # print(6 in a)
#
# # Linear search using 'count'
# # print(a.count(10) > 0)
# #
# # # Binary search using bisect
# # pos = bisect.bisect_right(a, 8)
# # print("Found at index:", pos)
# class Solution:
#     def isSorted(self, arr) -> bool:
#         for i in range(0,len(arr)-1):
#             if arr[i]>arr[i+1]:
#                 return False
#         return True
#
# solution = Solution()
# print(solution.isSorted([10,200,30,40,50]))

# class Solution:
#     def isBalanced(self, s):
#         # code here
#         while True:
#             if '[]' in s:
#                 s=s.replace('[]','')
#             elif '{}' in s:
#                 s=s.replace('{}','')
#             elif '()' in s:
#                 s=s.replace('()','')
#             else:
#                 return not s
#
# solution = Solution()
# print(solution.isBalanced("([{[]}])"))

# def getSecondLargest(arr):
#     max = arr[0]
#     for i in arr:
#         if i>max:
#             max= i
#     return max
# arr = [12, 35, 1, 10, 34, 1]
# print(getSecondLargest(arr))

# def sum_array(arr):
#     sum=0
#     for i in range(0,len(arr)):
#         sum+=arr[i]
#     return sum
#
# print(sum_array([1,2,3,4]))

# def palindrome(n):
#     start = 0
#     end = len(n)-1
#     while start<end:
#         if n[start]<n[end]:
#             return False
#         start+=1
#         end-=1
#     return True
#
# # print(palindrome(["abccba"]))
#
# def main(n):
#     if n == n[::-1]:
#         return True
#     return False
# print(main('k'))

# def digit_sum(n):
#     while n>=10:
#         n = sum(int(i) for i in str(n))
#     return n
#
# # print(digit_sum(987)) #24
#
#
# def digit_sum(n):
#     #1+(n-1)%9
#     if n==0:
#         return 0
#     else:
#         return 1+(n-1)%9
#
# print(digit_sum(987))

# from collections import ChainMap,Counter
# d1 = {'a':1,'b':2,'c':3,'f':4,'a':20}
# d2 = {'a':1,'b':2,'c':13,'d':10}
#
# d3 = ChainMap(d1,d2)
# d4 = Counter(d1)
# d = {**d1,**d3}
# empty_dict = {}
# for k,v in d1.items():
#     if k in empty_dict:
#         d[k] = empty_dict.get(k,0) +v
#     else:
#         d[k] = v
# print(empty_dict)
# print(d3)
# print(d4)

# s = 'abcdefgh'
# print(s[::-1])

# x = [1,2,3,4,5,6,7,8,9,10]
# d = {i: i+1 for i in x if i%2!=0}
# print(d)

#how add the dictnory like odd number as key and Even number as value

#
# csv.reader(file)
# csv.writer(file)
# csv.DictReader(file)
# csv.DictWriter(file)
# json.load(file)
# json.dump()
# json.dumps(file)
# json.loads(file)

# arr1=[1001001011]
# arr2=[1110010101]
#
# arr1 = [int(i) for i in str(arr1[0])]
# arr2 = [int(i) for i in str(arr2[0])]
# count = 0
# count1 = 0
#
# for i,j in zip(arr1,arr2):
#     if i==j:
#         count+=1
#     else:
#         count1+=1
# print(count)
# print(count1)

# arr = [1, 2, 4, -1, 5, -5, 7, 8, -9, -2]
# k = 3
#
# for i in range(len(arr)-k+1):
#     window = arr[i:i+k]
#     val = window[0]
#     if val>0:
#         print(f"veg pizza:",{str(window):val})
#     else:
#         print(f"non-veg pizza:",{str(window): val})


# def fib(n):
#     a,b=0,1
#     for i in range(n):
#         yield a
#         a,b = b,a+b
# for i in fib(10):
#     print(i)

# def fi(n):
#     if n<=1:
#         return n
#     return fi(n-1)+fi(n-2)
#
# for i in range(10):
#     print(fi(i))

# def max_element(lst):
#     l = len(lst)
#     for i in range(l):
#         for j in range(0,l-i-1):
#             if lst[j]>lst[j+1]:
#                 lst[j],lst[j+1] = lst[j+1],lst[j]
#     return lst
# print(max_element([1,20,3,5,6,9]))

# s = "[()()]{}"
# def checker(s):
#     while True:
#         if "[]" in s:
#             s=s.replace("[]","")
#         elif "()" in s:
#             s=s.replace("()",'')
#         elif "{}" in s:
#             s=s.replace("{}","")
#         else:
#             return not s
# s = "[()()]{}"
# print(checker(s))



# class Solution:
#     def isBalanced(self, s):
#         # code here
#         while True:
#             if '[]' in s:
#                 s=s.replace('[]','')
#             elif '{}' in s:
#                 s=s.replace('{}','')
#             elif '()' in s:
#                 s=s.replace('()','')
#             else:
#                 return not s
#
# solution = Solution()
# print(solution.isBalanced("([{[]}])"))


from collections import deque

# def delete_item(s):
#     v = []
#     while s:
#         v.append(s.pop())
#     mid = len(v)//2
#     v.pop(mid)
#     for i in range(len(v)-1,-1,-1):
#         s.append(v[i])


class Stack:
    def __init__(self):
        self.stack_items = []
        self.items=0
    def push(self,data):
        self.stack_items.append(data)
        return f"items pushed to the Stack{data}."
    def pop(self):
        self.stack_items.pop()
        return f"items popped from the stack{self.stack_items.pop()}."
    def length(self):
        return f"items length of the stack{len(self.stack_items)}"

# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)
# s.push(7)
# s.pop()
# # print(s.stack_items)
# # s.pop()
# s.pop()
# # s.pop()
# # s.pop()
# # s.pop()
# # print(s.stack_items)
# s.length()
# print(s.stack_items)




