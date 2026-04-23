# Reverse a number
# def reverse_number(num):
#     reverse = 0
#     while num >0:
#         digit = num % 10
#         reverse = reverse *10+digit
#         num//=10
#     return reverse
# #print(reverse_number(1234567))
# ---------------------------------------------------
#fibonacci series

# 👉 Question: Print first n Fibonacci numbers
# def fibanocci_num(n):
#     if n<=1:
#         return n
#     a,b = 0,1
#     for i in range(2,n):
#         a,b=b,a+b
#         print(a)
# fibanocci_num(10)
# ----------------------------
# 🔹 2. Fibonacci using recursion
#
# 👉 Question: Find nth Fibonacci number using recursion
#
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)
#
# print(fib(6))
# 🔹 3. Fibonacci using dynamic programming (optimized)
#
# 👉 Question: Avoid repeated calculations
#
# def fib(n):
#     dp = [0, 1]
#     for i in range(2, n+1):
#         dp.append(dp[i-1] + dp[i-2])
#     return dp[n]
#
# print(fib(10))

# --------------------------
# def fib(n):
#     dp = [0, 1]
#     for i in range(2, n+1):
#         dp.append(dp[-1] + dp[-2])
#     return dp
#
# print(fib(10))
# --------------------------------------------------------------------------------------
from fastapi import FastAPI
from collections import Counter
app = FastAPI()

@app.post("/")
def find_repeating_words(payload: str):
    # Convert string into list of words
    words = payload.split()

    # Count occurrences
    word_count = Counter(words)

    # Filter repeating words (count > 1)
    repeating_words = {word: count for word, count in word_count.items() if count > 1}

    return {
        "input": payload,
        "repeating_words": repeating_words
    }
# ---------------------------------------------------------------------
s = "aabcccccaaa"

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1

# add last character
result += s[-1] + str(count)
# -------------------------------------------------------------------------
# Adding two lists
def add_list(l1,l2):
    return l1+l2

l1 = [1,2,3,4]
l2 = [5,6,7,8]

# print(add_list(l1,l2))
# --------------------------------------------------------------------------
#Remove duplicates from list
def remove_duplicates(l):
    lst = []
    lst1 = []
    for i in l:
        if i not in lst:
            lst.append(i)
        else:
            lst1.append(i)
    return lst
l =  [1,2,3,3,2,1,4,5,6,6,7]
# print(remove_duplicates(l))
#----------------------------------------------------------------------------
#sort the list

def sorting(l):
    l.sort()
    return l
l = [10,2,30,3,1,9,20]
# print(sorting(l))
# ----------------------------------------------------------------------------
#Reverse a list

def reversing(l):
    l.reverse()
    return l
l = [10,2,30,3,1,9,20]
#print(reversing(l))
# ---------------------------------------------------------------------------
#count occurrence of an element

def count_occur(l):
    return l.count(3)
l = [10,2,30,3,1,9,20,3,3,3]
#print(count_occur(l))
# ----------------------------------------------------------------------------
#sum of elements in list

def sum_of(l):
    return sum(l)
l = [10,2,30,3,1,9,20,3,3,3]
#print(sum_of(l))
# -----------------------------------------------------------------------------
#palindrome string

def pal(l):
    rev = ""
    for i in l:
        rev = rev+i
        # return rev
    if rev==l:
        return True
    else:
        return False
# print(pal("racecar"))
# --------------------------------------------------------------------------------
#Happy number
def happy_number(n):
    if(n==1 or n==7):
        return True
    elif (n<10):
        return False
    else:
        sum = 0
        while(n>0):
            temp = n%10
            sum = temp*temp
            n=n//10
        return happy_number(sum)
# print(happy_number(1231))
# --------------------------------------------------------------------------------------
def modify(lst):
    lst.append(7)
    lst = [1,2]

nums = [0]
modify(nums)
# print(nums)
# ----------------------------------------------------------------------------------------
#longest consecutive sequence
def longest(num):
    num_set = set(num)
    longest_seq = []

    for num in num_set:
        if num - 1 not in num_set:
            current_num  = num
            current_seq = [current_num]

            while current_num+1 in num_set:
                current_num +=1
                current_seq.append(current_num)

            if len(current_seq)>len(longest_seq):
                longest_seq = current_seq
    return longest_seq
print(longest([100,4,300,1,2,3]))
# ------------------------------------------------------------------------------------------
result = [[1,2,3],[4,4,2],[1,5,6]]
data = [ j for i in result for j in i]
# print(data)
# --------------------------------------------------------------------
# Accept a number user check whether it is prime or not?

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n = int(input("Enter number : "))

if is_prime(n):
    print(f"prime number: {n}")
else:
    print(f"{n} is not a prime number")

# ---------------------------------------------
def checking():
    string = "silent1"
    string1 = "listen"
    if sorted(string)==sorted(string1):
        return True
    else:
        return False
# print(checking())
# ----------------------------------------------------------------------
def deco1(func):
    def wrapper():
        print("deco1 before")
        func()
        print("deco1 after")

    return wrapper


def deco2(func):
    def wrapper():
        print("deco2 before")
        func()
        print("deco2 after")

    return wrapper


@deco1
@deco2
def say_hello():
    print("Hello!")

print(say_hello())
# --------------------------------------------------------------------------
# Accept a number user check whether it is prime or not?

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n = int(input("Enter number : "))

if is_prime(n):
    print(f"prime number: {n}")
else:
    print(f"{n} is not a prime number")
# -----------------------------------------------------------------------
def longestPalindrome(s):
    if len(s) < 1:
        return ""

    start = 0
    end = 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = expand(i, i)      # odd length
        len2 = expand(i, i + 1)  # even length
        max_len = max(len1, len2)

        if max_len > end - start+1:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end+1]

print(longestPalindrome("babad"))
# -----------------------------------------------------------------------
s1 = [s[max(i-3,0):i] for i in range(len(s),0,-3)[::-1]]
print(','.join(s1))

spl1 = []
for i in range(len(s), 0, -3):
    start = max(i-3, 0)
    spl1.append(s[start:i])

s =9154369638
sp = []
for i in range(len(str(s)),0,-3):
    start = max(i-3,0)
    sp.append(str(s)[start:i])
# -----------------------------------------------------------------------
def isvalid(s):
    stack = []
    pairs = {"}":"{",")":"(","]":"["}

    for i in s:
        if i in pairs.values():
            stack.append(i)
        elif i in pairs.keys():
            if not stack or stack[-1]!=pairs[i]:
                return False
            stack.pop()
    return len(stack)==0
# --------------------------------------------------------------------------
# #1.Reversing string
# s = "reverse python string development"

# rev = s.split(' ')[::-1]
# final_data = ' '.join(rev)
# print(final_data)
# -----------------------------------------------------------------------------
#2.find duplicates from list
# def finding_duplicates():
#     lst = [1,2,3,4,4,5,2,10,10]
#     duplicates_removed_= list(set(lst))
# print(duplicates_removed_)
# -----------------------------------------------------------------------------
# lst = [1,2,3,4,1,2,5,6,6,7]
# print(list(dict.fromkeys(lst)))
# non_dup_list = []
# dup_lst=[]
# for i in lst:
#     if i not in non_dup_list:
#         non_dup_list.append(i)
#     else:
#         dup_lst.append(i)
# print(dup_lst)
# print(finding_duplicates())
#---------------------------------------------
# #3.reverse integer number
# nums = 1234567
# # print(str(nums)[::-1])
#
# #4.reverse integer number using different number
#
# def reverse_number(num):
#     reverse = 0
#     while num >0:
#         digit = num % 10
#         reverse = reverse *10+digit
#         num//=10
#     return reverse
# #print(reverse_number(1234567))
#-----------------------------------------------------------------
# #5.sum of numbers without using predefined methods
#
# def sum_numbers(a,b):
#     while b!=0:
#         data = a&b
#         a =a^b
#         b = data<<1
#     return a
# # print(sum_numbers(10,2))
#------------------------------------------------------------------
# #6.fibanocci series
# def fib(n):
#     if n<0:
#         return 0
#     elif n==0:
#         return 0
#     elif n==1:
#         return 1
#     a,b = 0,1
#     for i in range(2,n+1):
#         a,b=b,a+b
#     return b
# # for i in fib(10):
# #     print(i)
#--------------------------------------------------------------------
# #7.identify the duplicates in list
# lst = ["req1","req2","req3","req4","req5","req1","req3"]
#
# dup_lst = []
# l = []
#
# for i in lst:
#     if i not in l:
#         l.append(i)
#     else:
#         dup_lst.append(i)
# #print(dup_lst)
#-----------------------------------------------------------------------------
# #8.recursion function
# # Recursion is a technique where the function calls itself.
# def recursion_p(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * recursion_p(n-1)
#         #1*(1-1) #0,
#         # 2*(2-1) #2
#         # 3*(3-1) #6
#         # 4*(4-1) #12
#         # 5*(5-1) #20
# recur = recursion_p(5) #
# # print(recur)
#-------------------------------------------------------------------------------
# #9.sum of the values in dictionary
# dictionary = [("apple",100),("orange",200),("apple",500),("apple",400),("banana",100)]
#
# empty_dict = {}
#
# for key,value in dictionary:
#     if key not in empty_dict:
#         empty_dict[key] = 0
#     empty_dict[key]+=value
# # print(empty_dict)
#---------------------------------------------------------------------------------------
# #10.using default dictionary to sum the dictionary values
# dictionary = [("apple",100),("orange",200),("apple",500),("apple",400),("banana",100)]
#
# from collections import defaultdict
#
# data = defaultdict(int)
#
# for key,value in dictionary:
#     data[key]+=value
# # print(data)
# #10.using get method in dictionary to sum the values in dictionary
# dictionary = [("apple",100),("orange",200),("apple",500),("apple",400),("banana",100)]
# empty_dict = {}
# for key,value in dictionary:
#     empty_dict[key] = empty_dict.get(key,0) +value
#
# # print(empty_dict)
#----------------------------------------------------------------------------------------
# #11.generators
# def large_file_read(filepath):
#     with open(filepath,"r") as filename:
#         file_data =filename.readlines()
#         for i in file_data:
#             yield i
#
#
# #for i in large_file_read(r"C:\Users\shiva\PycharmProjects\PythonProject\customers-100.csv"):
#     # print(i)
#-------------------------------------------------------------------------------------------
# #11.reading csv files
# import csv
#
# def reading_csv_file():
#     with open(r"C:\Users\shiva\PycharmProjects\PythonProject\customers-100.csv",'r') as file:
#         reader = csv.DictReader(file)
#         for i in reader:
#             yield i
# data = reading_csv_file()
# # print(next(data))
# # print(next(data))
# # print(next(data))
#---------------------------------------------------------------------------------------------
# #12.find second highest number
# remove_lst = [1,2,10,29,30,32,7,4,9,90,80]
# remove_lst = list(set(remove_lst))
# remove_lst.sort(reverse=True)
# #print(remove_lst[1])
#---------------------------------------------------------------------------------------------
# #13.word count
# string_data = "venkat python developer AI engineering python venkat"
#
# word_count = {}
# data_splitting = string_data.lower().split()
#
# for i in data_splitting:
#     if i in word_count:
#         word_count[i]+=1
#     else:
#         word_count[i]=1
#
# # print(word_count)
#-------------------------------------------------------------------------------------------------
# #14. flatten list
#
# lst = [[1,2,3],3,4,[5,6],[1,7,8,9]]
# flattened_lst = []
# for i in lst:
#     if isinstance(i,list):
#             flattened_lst.extend(i)
#     else:
#         flattened_lst.append(i)
# # print(flattened_lst)
#---------------------------------------------------------------------------------------------------
# #15.iterating list of elements
# lst = [10,2,3,4]
#
# data = iter(lst)
# # print(next(data))
# # print(next(data))
# # print(next(data))
#----------------------------------------------------------------------------------------------------
# #16.list append dynamically
# def item_lst(item,lst=[]):
#     lst.append(item)
#     return lst
# # print(item_lst(1))
# # print(item_lst(2))
# # print(item_lst(3))
# # print(item_lst(4))
#------------------------------------------------------------------------------------------------------
# nums = [0, 1, 2, 3, 4, 5]
# # result = list(filter(bool, nums))
# result = [x for x in nums if x]
# # print(result)
# #17.split every 3 digits with coma
# num = 9154369638
# s= str(num)
#
# s1 = [s[max(i-3,0):i] for i in range(len(s),0,-3)[::-1]]
# # print(','.join(s1))
#
# # spl1 = []
# # for i in range(len(s), 0, -3):
# #     start = max(i-3, 0)
# #     spl1.append(s[start:i])
# #
# # spl1.reverse()
# # data =','.join(spl1)
# # print(data)
#-----------------------------------------------------------------------
# #18. split negative and positive numbers based on if else conditions
# lst = [1,2,3,4,-3,-9,1,-1,7]
# k= 4
# for i in range(len(lst)-k+1):
#     window = lst[i:i+k]
#     value = window[0]
#     if value>0:
#         pass
#         #print(f"veg:",{str(window):value})
#     else:
#         pass
#         #print(f"non veg:",str({str(window):value}))
#------------------------------------------------------------------------
# arr = [10,30,20,90,40,50]
# for i in range(0,len(arr)-1):
#     if arr[i]>arr[i+1]:
#         arr[i],arr[i+1] = arr[i+1] ,arr[i]
# # print(arr)
#-------------------------------------------------------------------------
# #19.generate a prime numbers using generators
# def isprime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#         return True
#
# def gen(n):
#    j=2
#    while n:
#        if isprime(i):
#            yield i
#            n-=1
#        j+=1
#
# gen = gen(10)
# # print(next(gen))
# -------------------------------------------------------------------------------
# #20.splitting multilines
#
# str_data = """100,10,login
# 200,20,logout
# 300,30,login
# 400,40,logout
# 500,50,login
# 600,60,logout
# 700,70,login"""
#
# times = {}
# session = {}
#
# for data1 in str_data.splitlines():
#     user_id,time,action = [i.strip() for i in data1.split(',')]
#     final_data = int(time)
#
#
#     if action =='login':
#         times[user_id] = time
#     else:
#         if action == 'logout':
#             if user_id in times:
#                 session[user_id] = final_data - times[user_id]
# # print(times)
#--------------------------------------------------------------------------
# def reverse_digit(n):
#     reversed_num = 0
#     while n>0:
#         digit = n%10
#         reversed_num = reversed_num*10+digit
#         n = n//10
#     return reversed_num
#
# # print(reverse_digit(9154369638))
#--------------------------------------------------------------------------
# #21.MultiThreading vs MultiProcess
#
# #i) MultiThreading : Allows multiple threads in single process
# #ii) Good for i/o operation
# #iii)Limited by the GIL
#
# # MultiProcess:   Runs separate processes, each with its own python interpreter
# # can achieve true parallelism
# #suitable for CPU - bound tasks
#----------------------------------------------------------------------------
# #22.3D matrix
# first_loop = []
# for i in range(3):
#     second_loop = []
#     for j in range(4):
#         third_loop = []
#         for k in range(6):
#             third_loop.append("venkat")
#         second_loop.append(third_loop)
#     first_loop.append(second_loop)
#-----------------------------------------------------------------------------
# #23.function calling multiple return statements
# def multiple_returns():
#     name = "venkat"
#     age = 27
#     marital_status = "Single"
#
#     return name,age,marital_status
#
# c = multiple_returns()
# name,age,marital_status = multiple_returns() #c
# # print(name,age,marital_status)
#----------------------------------------------------------------------------------
# # 24.In python all arguments are passed by reference means if any mutable objects changed it will be reflected to outside as well
# def pass_by_reference(lst):
#     lst.append([1,2,3,4])
#     return lst
#
# lst = [10,20,30,40]
# # print(pass_by_reference(lst))
#----------------------------------------------------------------------------------
# #25. In python pass by value won't work it will override the values
#
# def pass_by_value(lst):
#     lst = [1,2,3,4]
#     # print(lst.append(lst))
#     # print(f"inside the function variables  : {lst}")
#
# lst = [10,20,30,40]
# pass_by_value(lst)
# print(f"outside the variables : {lst}")
# print(pass_by_value(lst))
#------------------------------------------------------------------------------------
# #26.function parameter vs arguments
#
# #1.Parameter ==>> parameter is the value which we passed inside the function definition(inside parenthesis).
# #2.Argument ==>> Argument in function is value which we are passing while calling time.
#
# #27.reduce function
#
# from functools import reduce
#
# lst = [10,20,30,40,79]
#
# # print(reduce(lambda x,y: x+y,lst))
# # print(list(map(lambda x:x*2,lst)))
# # print(list(filter(lambda x:x%2==0,lst)))
#
# #28.yaml file creation
# import yaml
#
# data = {"name":"venkat","age":27,"marital_status":"Single"}
#
# converting_to_yaml = yaml.dump(data)
# # print(converting_to_yaml)
#
#
# # def main_function(func):
# #     def wrapper(*args,**kwargs):
# #         print("wrapper function")
# #         data = func(*args,**kwargs)
# #         return data
# #     return wrapper
#
# # @main_function
# # def inner_function():
# #     return True
#
# # print(inner_function())
#
# # emp: emp_id, name, dept_id, salary
#
# # dept: dept_id. dept_name
#
# # query: Name of dept which is spending max on salary.
#
# # select e.emp_id, e.name, e.dept_id, max(e.salary) As max_salary ,d.dept_id. d.dept_name
#
# # FROM emp e join dept d on e.dept_id=d.dept_id
#
# # group by d.dept_name;
#
# # from fastapi import FastAPI
# # import asyncio
#
# # app = FastAPI()
#
# # @app.post("/")
# # async def calling_function():
# #     count = 0
# #     for  i in range(0,3):
# #         await asyncio.time(300) #5*60
# #         count +=1
# #         print(f"No of times function executed:{count}")
#
#
# # import time
# # def calling():
# #     count = 0
# #     for i in range(0, 3):
# #         time.sleep(1)
# #         count += 1
# #         print(f"No of times function executed:{count}")
# # calling()
#
#
# # my_list = [2, 3, 5, 7, 11]
# # data = {i:j*j for i,j in enumerate(my_list)}
# # print(data)
#
#
# # pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
# # for p in pat:
# #   pass
# #   if (p == 0):
# #       current = p
# #       break
# #   elif (p % 2 == 0):
# #       continue
# #   print(p)
# # print(current)
#
# # lst = [1, 2, 8, 4, 16, 77, 7]
#
# # lst.sort(reverse= True)
# # print(lst[1])
#
# # data = lst.sorted)
#
# # class A:
# #     def who(self):
# #         print("A")
# #
# #
# # class B(A):
# #     def who(self):
# #         print("B")
# #
# #
# # class C(A):
# #     def who(self):
# #         print("C")
# #
# #
# # class D(B, C):
# #     pass
# #
# #
# # d = D()
# # d.who()
# # print(D.mro())
#
# lst1 = [1,2,3,4]
# data = sum(lst1)
# # print(data)
#
# total = 0
# for i in lst1:
#     total+=i
# # print(total)
# # check the matrix is squared or not
# mat = [[1,2],[3,4],[5,6]]
# rows = len(mat)
# cols = len(mat[0])
# # print(rows,cols)
# # if rows ==cols:
# #     print("Matrix is squared")
# # else:
# #     print("Matrix is not squared")
#
# # check diagonal matrix
# s = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# for i in range(len(s)):
#     for j in range(len(s)):
#         if i==j:
#             print(s[i][j],end = ',')

# s = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# l = len(s)
# for i in range(l):
#     for j in range(l):
#         if i+j == l-1:
#             print(s[i][j],end =',')

# matrix = [[1,2],[3,4]]
#
# for i in range(len(matrix)):
#      for j in range(len(matrix)):
#           if matrix[j][i]:
#                print(matrix[j][i],end = ', ')



# def fibonacci(n):
#      fib = [0, 1]
#      for i in range(n):
#           fib.append(fib[-1]+fib[-2])
#      print(fib)
# fibonacci(5)

# move zero's to end of the list

# non_zero_array = [1,2,0,8,0,7,0,0,6,5]
# for i in non_zero_array:
#     if i==0:
#         non_zero_array.append(i)
#         non_zero_array.remove(i)
#     else:
#         continue
# print(non_zero_array)

# print(bool("False")) True
# from functools import reduce
# lst = [1,2,3,4,5,6,7,1,9,20,12,0]
# print(list(map(lambda x:x*x,lst)))
# print(list(filter(lambda x:x<10,lst)))
# df = reduce(lambda  x,y:x+y,lst)
# # print(df)
# print(sorted(lst,reverse=True))
# lst.sort(reverse=False)
# print(lst)

# lst_items = [1,2,3,4,5]
# data = iter(lst_items)
# for i in data:
#     print(i)

#
# class Gen:
#
#     def __init__(self,num):
#         self.num = num
#
#     def generate(self):
#         for ins in range(0,self.num):
#             yield ins
#
# gen = Gen(10)
# for i in gen.generate():
    # print(i)
# class Gen:
#     def __init__(self,num):
#         self.num = num
#
#     def __iter__(self):
#         for ins in range(0,self.num):
#             yield ins
#
# gen = Gen(10)
# for i in gen:
#     print(i)
# class Gen:
#     def __init__(self,num):
#         self.num = num
#
#     @property
#     def generating(self):
#         for ins in range(0,self.num):
#             yield ins
#
# gen = Gen(10)
# for i in gen.generating:
#     print(i)

# d=  list(i for i in range(10))
#
# for i in d:
#     print(i,end = ' : ')
#
# for i in d:
#     print(i)

# if __name__ =='__main__':
#     n = int(input())
#     empty_list = []
#     for i in range(n):
#         command , *args = input().split()
#         if command =='print':
#             print(empty_list)
#         elif command == 'append':
#             empty_list.append(i)
#         elif command =='remove':
#             empty_list.remove(i)
#         elif command =='sort':
#             empty_list.sort()
#         elif command =='pop':
#             empty_list.pop()
#         elif command == 'reverse':
#             empty_list.reverse()
#         elif command =='clear':
#             empty_list.clear()
#         elif command =='extend':
#             empty_list.extend([i])
#         elif command =='count':
#             empty_list.count(i)
#         elif command =='insert':
#             empty_list.insert(0,i)
#     print(empty_list)
# s1={1,2,3}
# s2={3,4,5}
# print(s1|s2) #union
# print(s1&s2) #intersection
# print(s1-s2)

############################
# from pprint import pprint
#
# class Iteration:
#     def __init__(self,num):
#         self.num = num
#         self.current = 0
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current<self.num:
#             self.current+=1
#             return self.current
#         raise StopIteration
#
# it = Iteration(10)
# for i in it:
#     pprint(i)
#
# import threading
#
# def print_numbers():
#     for i in range(0,1000):
#         print(i)
#
#
# threading1 = threading.Thread(target=print_numbers)
# threading2 = threading.Thread(target=print_numbers)
#
# threading1.start()
# threading2.start()
# #
# threading1.join()
# threading2.join()
# def outer_deco(n):
#     def inner_deco(func):
#         def wrapper(*args):
#             for i in range(n):
#                 func(*args)
#         return wrapper
#     return inner_deco
#
# @outer_deco(4)
# def calling_deco(a,b,c=10,d=20):
#     print(a,b,c,d)
#
# # calling_deco(5,4,90,89)
# # t = (1, 2, 3)
# # for i in t:
# #     i += 5
# # print(t)
#
# mytuple = ('Dave', 42, True)
# (one, *two, hey) = (1,4,2,8,2,2)
# # print(one, two, hey)
#
# lst = ["1","2","3"]
#
# lst+="4" #lst=lst+'3'
# print(lst)
#
# def isvalid(s):
#     stack = []
#     pairs = {"}":"{",")":"(","]":"["}
#
#     for i in s:
#         if i in pairs.values():
#             stack.append(i)
#         elif i in pairs.keys():
#             if not stack or stack[-1]!=pairs[i]:
#                 return False
#             stack.pop()
#     return len(stack)==0
# print(isvalid("{[()]}{"))
#
# class Node:
#     def __init__(self, key=0, value=0):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None
#
#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}  # key -> node
#
#         # Dummy head and tail
#         self.left = Node()   # LRU
#         self.right = Node()  # MRU
#
#         self.left.next = self.right
#         self.right.prev = self.left
#
#     # Remove node from list
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next = nxt
#         nxt.prev = prev
#
#     # Insert node at right (most recent)
#     def insert(self, node):
#         prev, nxt = self.right.prev, self.right
#         prev.next = node
#         node.prev = prev
#         node.next = nxt
#         nxt.prev = node
#
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].value
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#
#         node = Node(key, value)
#         self.cache[key] = node
#         self.insert(node)
#
#         if len(self.cache) > self.capacity:
#             # remove LRU node
#             lru = self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]


# def isValid(s):
#     stack = []
#     pairs = {')': '(', '}': '{', ']': '['}
#
#     for ch in s:
#         if ch in pairs.values():  # opening brackets
#             stack.append(ch)
#         elif ch in pairs:  # closing brackets
#             if not stack or stack[-1] != pairs[ch]:
#                 return False
#             stack.pop()
#
#     return len(stack) == 0

# array_elements = [1,20,2,3,10,4,40,50]
#
# for i in range(len(array_elements)):
#     for j in range(i+1,len(array_elements)):
#         if array_elements[i]>array_elements[j]:
#             array_elements[i],array_elements[j]=array_elements[j],array_elements[i]
# print(array_elements[-2])

# dictionary = {'name':1,'age':297,'marks':99}
#
# data = dict(sorted(dictionary.items(),key =lambda x:x[0]))
# print(data)
 # monkey patching
 #Dynamically modifying or extending a class or module at runtime.

# class Coding:
#     def calling_class(self):
#         print("Coding Questions")
#
# def calling_function(self):
#     print("calling Questions")
#
# Coding.calling_class = calling_function
#
# a = Coding()
# a.calling_class()

# print(bool(1))

# def unique(lst):
#     uniques = {}
#     for i in lst:
#         if i in uniques:
#             uniques[i]+=1
#         else:
#             uniques[i]=1
#
#     for key,value in uniques.items():
#         if value==1:
#             return key
#
# print(unique([0,1,2,2,3,4,5,6,7,8,9]))


# num = int(input("Enter a number: "))
#
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")
#
#
# def flatten(input):
#     final_output = []
#     for i in input:
#         if isinstance(i, list):
#             final_output.extend(flatten(i))
#         else:
#             final_output.append(i)
#     return final_output
# input = [1, [2, [3, 4, 5, [6, 7, 8, 9], 11], [1, 3, 5, 7]]] ## output: [1,2,3,4,5,6,7,8,11]
# print(flatten(input))
#
#In FastAPI, dependency override is mainly used to replace a dependency with another implementation, usually during testing or when you want to mock database/authentication/services.
# from fastapi.testclient import TestClient
#
# client = TestClient(app)
#
# def override_dependency():
#     return "Test Message"
#
# app.dependency_overrides[get_message] = override_dependency
#
# def test_api():
#     response = client.get("/")
#     assert response.json() == {"message": "Test Message"}


#In FastAPI
#1.JWT token implementation,OAuth2 Implementation
#2.Middlewares
#routing
#Background tasks
#fast api deployment ,docker .yaml file creation,deployment

# fastapi CORSMIiddlewares use cases and interview questions on this topic and coding question on CORSMiddlewares?
import time
from functools import wraps

def decorator_retry(attempts=5,delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for attempt in range(attempts):
                try:
                    func(*args,**kwargs)
                except Exception as e:
                    print(e)
                    if attempt == attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@decorator_retry(attempts=5,delay=2)
def final_call(a,b):
    return a+b

# print(final_call(1,2))


from functools import lru_cache,wraps

def decorator_retry(retry=3,delay=1):
    def inside_decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(retry):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                   if i == retry -1:
                       raise
                time.sleep(delay)
        return wrapper
    return inside_decorator

@lru_cache(maxsize=128)
@decorator_retry(retry=3,delay=1)
def session_call():
    return True

# print(session_call())
@lru_cache(maxsize=128)
def fibnocci(n):
    start_time = time.time()
    print(start_time)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib = [0,1]
    for i in range(n):
        fib.append(fib[-1]+fib[-2])
    end_time = time.time() - start_time
    print(end_time)
    return fib
# print(fibnocci(10))

#count how many times function called
call_counts = {}
def count_calls(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        # wrapper.calls += 1
        # print(wrapper.calls)
        call_counts[func.__name__] = call_counts.get(func.__name__, 0) + 1
        return func(*args,**kwargs)
    # wrapper.calls = 0
    return wrapper
# print(call_counts)

@count_calls
def calling():
    return True
# print(calling())
# print(calling())

#As a tech lead, your responsibility is to:

# Identify cross-cutting concerns
    #
    # retries
    #
    # auth
    #
    # logging
    #
    # tracing
    #
    # metrics
    #
# Move them into reusable decorators/context managers

# Enforce usage across services

# This prevents:
    #
    # duplicated logic
    #
    # inconsistent behavior
    #
    # hidden bugs

#A naive decorator replaces the original function with a wrapper ,which loses the metadata

    #function name
    #docstring
    #type hints
    #signature
    #example : function_name.__name__
# To prevent this weed to use @wraps(func)
# so it preservers:
    #__name__
    #__doc__
    #__annotations__
    #__module__
import asyncio
from functools import wraps

def log(func):
    if asyncio.iscoroutinefunction(func):
        @wraps(func)
        async def wrapper(*args,**kwargs):
            return await func(*args,**kwargs)
        return wrapper
    else:
        @wraps(func)
        def wrapper(*args,**kwargs):
            return func(*args,**kwargs)

        return wrapper

############################################################################
# Python Memory Management
    #Python primarily uses automatic memory manager. As a developer we no need to allocate or free memory
    #In Cpython memory manager consist of
        # Reference counting
        # Generational Garbage collection
        # private heap + Memory Allocator

        # Application Objects
        #         ↓
        # Reference Counting
        #         ↓
        # Garbage Collector(cycle detection)
        #         ↓
        # Python Private Heap
        #         ↓
        # OS Memory

#Note: Python uses reference count for immediate cleanup and garbage collection for cyclic references.
# when it reaches reference count 0 then it is immediately deallocated
# a = []
# b=a reference count 2
# del  a then reference count 1
import sys

# print(sys.getrefcount(a))
# print(sys.getrefcount(b))
# del b
# print(sys.getrefcount(b))

####################################
#even numbers vs odd number

list_of_numbers = [1,2,4,6]
even_numbers = []
odd_numbers = []
for number in list_of_numbers:
    if number%2==0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
odd = min(odd_numbers)
even  = max(even_numbers)
final_value = even - odd
# print(final_value)
#############################################


def flatten_dictionary(d, parent_key='', sep = '*'):
    final_dict = {}
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value,dict):
            final_dict.update(flatten_dictionary(value,new_key,sep=sep))
        else:
            final_dict[new_key] = value
    return final_dict
dictionary =  {
    "a": 1,
    "b": {"c": 2, "d": {"e": 3}},
    "f": 4
}

# print(flatten_dictionary(dictionary))
#You are given an unsorted list of integers, like this:

nums = [100, 4, 200, 1, 3, 2]
#Task:
#Write a function that returns the length of the longest consecutive

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start of a sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest
# ✅ Call the function and print the result
result = longest_consecutive(nums)
print(result)


# def maxLenSubarray(arr, k):
#     prefix_sum = 0
#     max_len = 0
#     prefix_map = {}
#
#     for i in range(len(arr)):
#         prefix_sum += arr[i]
#
#         if prefix_sum == k:
#             max_len = i + 1
#
#         if (prefix_sum - k) in prefix_map:
#             max_len = max(max_len, i - prefix_map[prefix_sum - k])
#
#         if prefix_sum not in prefix_map:
#             prefix_map[prefix_sum] = i
#
#     return max_len
#
#
# arr = [6,5,2,1,3,6]
# k = 6
# print(maxLenSubarray(arr, k))


#Decorators and use cases in production systems
# 1.Decorators are implement ->> Aspect-oriented-programming(AOP) style behavior
#2. They allow you to inject behavior around function calls without modifying the function itself.
# Decorator resolves typical production concerns:
    #logging - Centralized instrumentation
    #Authentication/Authorization - Security Enforcement
    #Retry logic - Resilience
    #Rate Limiting - API Protection
    #Caching - Performance
    #Metrics - Observability
    #Validation - Input Contracts
    #Feature flags - Controlled rollout

    #Instead of polluting business logic with infrastructure code ,decorators separate concerns cleanly.
# import time
# from functools import wraps
# import logging
#
# logging = logging.getLogger(__name__)
#
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         logging.info(f"{func.__name__}")
#         try:
#             return func(*args,**kwargs)
#         finally:
#             duration = time.time() - start
#             logging.info(f"{func.__name__},duration:{duration}")
#
#     return wrapper
#
# @decorator
# def sum_of(a,b):
#     return a+b
# print(sum_of(5,7))


# Context Manager?
# 1.Context manager controls resource lifecycle
# def file_opening():
#     with open("sample.txt","r") as f:
#         read = f.read()
#         print(read)

# print(file_opening())

# Context Manager solves

# files  - >> descriptor leaks
# DB connections  ->> pool exhaustion
#locks ->>deadlocks
#network sockets ->> resource leak
#trasanctions ->> partial commits

# context managers guarantee deterministic cleanup
#
# class Transaction:
#
#     def __enter__(self,db):
#         db.begin()
#
#     def __exit__(self,db,exc_type,exc,traceback):
#         if exc:
#             db.rollbck()
#         else:
#             db.commit()

# prevents in consistent data
# automatic rollback


# Production Benefits
#
# • Consistent logging
# • No duplicate boilerplate
# • Easy instrumentation across services
#
# Frameworks like FastAPI, Flask, Django internally rely on this pattern.
#
# Production Use Case 2 — Retry Logic
#
# Common in microservices and distributed systems.
#
# import time
# from functools import wraps
#
# def retry(attempts=3, delay=1):
#
#     def decorator(func):
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#
#             for attempt in range(attempts):
#                 try:
#                     return func(*args, **kwargs)
#
#                 except Exception as e:
#                     if attempt == attempts - 1:
#                         raise
#
#                     time.sleep(delay)
#
#         return wrapper
#
#     return decorator
#
# Usage:
#
# @retry(attempts=5, delay=2)
# def call_payment_service():
#     ...
# Production Benefit
#
# Handles:
#
# • transient network failures
# • service unavailability
# • flaky APIs
#
# Libraries like tenacity use this exact concept.
#
# Production Use Case 3 — Authentication / Authorization
#
# Widely used in web frameworks.
#
# Example:
#
# def require_admin(func):
#
#     @wraps(func)
#     def wrapper(user, *args, **kwargs):
#
#         if not user.is_admin:
#             raise PermissionError("Admin required")
#
#         return func(user, *args, **kwargs)
#
#     return wrapper
#
# Usage:
#
# @require_admin
# def delete_user(user, user_id):
#     ...
#
# Production advantages:
#
# • Security policy centralized
# • Easy enforcement across endpoints
#
# Production Use Case 4 — Caching
#
# Used in performance-critical workloads.
#
# Python provides built-in decorator:
#
# from functools import lru_cache
#
# @lru_cache(maxsize=1000)
# def expensive_calculation(x):
#     ...
#
# Production use:
#
# • ML feature computation
# • configuration lookup
# • metadata fetches
#
# Decorators in Major Frameworks
# Framework	Example
# Flask	@app.route()
# FastAPI	@app.get()
# Django	@login_required
# Celery	@shared_task
# PyTest	@pytest.fixture
#
# Example from FastAPI:
#
# @app.get("/users")
# def get_users():
#     ...
#
# @app.get registers route metadata via decorator.
#
# Advanced Decorator Patterns
# 1. Class Decorators
#
# Used to modify class behavior.
#
# Example:
#
# def singleton(cls):
#
#     instances = {}
#
#     def get_instance(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return get_instance
#
# Usage:
#
# @singleton
# class DBConnection:
#     pass
# 2. Stacked Decorators
#
# Multiple concerns applied sequentially.
#
# @retry()
# @log_execution
# @metrics
# def fetch_data():
#     ...
#
# Execution order:
#
# metrics(log_execution(retry(fetch_data)))
# Pitfalls with Decorators
# 1. Lost function metadata
#
# Fix:
#
# from functools import wraps
# 2. Debugging complexity
#
# Stack traces can become harder.
#
# 3. Hidden side effects
#
# Too many decorators → unreadable behavior.

# 1.5 Rate Limiting / Circuit Breaking

# Decorators can implement:
#
# rate limiting
#
# circuit breakers
#
# request throttling
#
# These are common in API gateways and microservices.
# Benefits
#
# Guarantees rollback on failure
#
# Avoids forgotten commits
#
# Clean transactional boundaries
#
# Used in:
#
# SQLAlchemy
#
# Django ORM
#
# internal database libraries

# from functools import lru_cache,wraps
#
# def decorator(retry=3,delay=1):
#     def inside_decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             for i in range(retry):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                    if i == retry -1:
#                        raise
#                 time.sleep(delay)
#
# @decorator(retry=3,delay=1)
# def session_call(a,b):
#     return a+b
#
# session_call(10,20)





###2. Context Managers in Production Systems

# Context managers control resource lifecycle.
#
# Typical pattern:
#
# with resource() as r:
#     use(r)
#
# Equivalent to:
#
# setup
# try:
#    block
# finally:
#    cleanup
# Problem Context Managers Solve
#
# Production code frequently deals with:
#
# Resource	Risk
# Files	descriptor leaks
# DB connections	pool exhaustion
# Locks	deadlocks
# network sockets	resource leak
# transactions	partial commits
#
# Context managers guarantee deterministic cleanup.
#
# Basic Context Manager Example
# with open("file.txt") as f:
#     data = f.read()
#
# Equivalent:
#
# f = open("file.txt")
# try:
#     data = f.read()
# finally:
#     f.close()
# Production Use Case 1 — Database Transactions
#
# Example:
#
# with db.transaction():
#     create_order()
#     charge_payment()
#
# Implementation:
#
# class Transaction:
#
#     def __enter__(self):
#         db.begin()
#
#     def __exit__(self, exc_type, exc, tb):
#         if exc:
#             db.rollback()
#         else:
#             db.commit()
#
# Production benefit:
#
# • prevents inconsistent data
# • automatic rollback on error
#
# Production Use Case 2 — Locks / Concurrency
#
# Thread safety:
#
# from threading import Lock
#
# lock = Lock()
#
# with lock:
#     critical_section()
#
# Equivalent manual code:
#
# lock.acquire()
# try:
#     ...
# finally:
#     lock.release()
#
# Used heavily in:
#
# • multi-threaded services
# • schedulers
# • caches
#
# Production Use Case 3 — Temporary Configuration
#
# Example:
#
# with set_env("DEBUG", "true"):
#     run_tests()
#
# Custom context manager:
#
# import os
#
# class set_env:
#
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#
#     def __enter__(self):
#         self.old = os.getenv(self.key)
#         os.environ[self.key] = self.value
#
#     def __exit__(self, *args):
#         if self.old:
#             os.environ[self.key] = self.old
# Production Use Case 4 — Performance Timing
# with timer("data_load"):
#     load_data()
# Context Managers Using contextlib
#
# Python provides a simpler approach.
#
# from contextlib import contextmanager
#
# @contextmanager
# def timer(name):
#
#     start = time.time()
#     yield
#     print(name, time.time() - start)
#
# Usage:
#
# with timer("task"):
#     process()
# Decorators vs Context Managers
# Aspect	Decorator	Context Manager
# Scope	Entire function	Block of code
# Syntax	@decorator	with
# Use Case	Cross-cutting function behavior	Resource lifecycle
# Control	Function invocation	Code block execution
#
# Example difference:
#
# Decorator:
#
# @retry
# def call_api():
#
# Context manager:
#
# with retry_context():
#     call_api()
# When To Use Each (Production Decision)
#
# Use decorators when:
#
# • behavior applies to function boundaries
# • used across many functions
# • enforcing policies
#
# Examples:
#
# authentication
#
# caching
#
# retries
#
# metrics
#
# Use context managers when:
#
# • controlling resource lifetime
# • code block specific behavior
#
# Examples:
#
# transactions
#
# locks
#
# files
#
# temporary state
#
# Combining Both (Advanced Pattern)
#
# Example in production frameworks.
#
# Decorator:
#
# @transactional
# def create_order():
#
# Inside implementation:
#
# with db.transaction():
#
# Decorator provides API, context manager handles resource management.
#
# Real Production Architecture Example
#
# Example microservice stack:
#
# @metrics
# @retry
# @timeout
# @auth_required
# def process_order():
#
# Inside:
#
# with db.transaction():
#     update_inventory()
#     charge_payment()
#
# Benefits:
#
# • clean business logic
# • centralized cross-cutting concerns
# • safe resource management
#
# Design Advice for Tech Leads
# 1. Limit decorator depth
#
# Too many decorators create invisible behavior.
#
# Rule of thumb:
#
# <= 3 decorators
# 2. Always preserve metadata
#
# Use:
#
# @wraps(func)
# 3. Keep decorators pure
#
# Avoid:
#
# global state mutation
# 4. Prefer context managers for resources
#
# Never hide resource control in decorators.
#
# Summary
# Concept	Key Role
# Decorators	Inject behavior around functions
# Context Managers	Manage resource lifecycle
# Decorators	Cross-cutting concerns
# Context Managers	Deterministic cleanup
#
# Production systems rely on both to achieve:
#
# • clean architecture
# • reusability
# • fault tolerance
# • observability
#
# If you'd like, I can also explain 3 advanced topics that senior engineers are often asked in staff/principal interviews:
#
# 1️⃣ How FastAPI and Flask internally implement decorators
# 2️⃣ Building distributed tracing decorators (OpenTelemetry)
# 3️⃣ Async context managers and async decorators in modern Python systems
#
# These are very common Staff Engineer interview topics. 🚀



# from contextlib import contextmanager
#
#
# @contextmanager
# def transaction(session):
#     try:
#         yield session
#         session.commit()
#     finally:
#         session.rollback()
#         session.close()

# Production examples:

    # database connections
    #
    # Redis clients
    #
    # Kafka producers
    #
    # thread locks
    #
    # temporary directories

# Use decorators when behavior belongs to the function.
# Use context managers when behavior belongs to a specific block of work.

from itertools import combinations
#
input = [["E1","ProjectA"],
         ["E2","ProjectB"],
         ["E1","ProjectB"],
         ["E3","ProjectA"],
         ["E2","ProjectA"]]


# emp_projects ={}
# for key,value in input:
#     if value in emp_projects:
#         emp_projects[key].append(value)
#     else:
#         emp_projects[key]=[value]
# print(emp_projects)
emp_projects = {}
for emp, proj in input:
    emp_projects.setdefault(emp, []).append(proj)


result = {}

for e1, e2 in combinations(emp_projects.keys(),2):
    common = list(set(emp_projects[e1]) & set(emp_projects[e2]))
    if common:
        result[f"{e1},{e2}"] = common

# print(result)
# data = [
#   ["C1", "Laptop"],
#   ["C2", "Phone"],
#   ["C1", "Phone"],
#   ["C3", "Laptop"],
#   ["C2", "Laptop"]
# ]
#
# # Step 1: customer -> products
# customer_products = {}
#
# for customer, product in data:
#     customer_products.setdefault(customer, set()).add(product)
#
# # Step 2 & 3: compare customer pairs
# result = {}
#
# for c1, c2 in combinations(customer_products.keys(), 2):
#     common_products = list(customer_products[c1] & customer_products[c2])
#     if common_products:
#         result[f"{c1},{c2}"] = common_products
#
# print(result)
# Example Input:
# lst = [1, 3, 4, 2, 2,3,3,4,6,5]
# seen = set()
# s=[]
# for i in lst:
#     if i not in seen:
#         seen.add(i)
#     else:
#         s.append(i)
# print(seen)
# print(s)

import re
text  ="kik"

def palindrome(text):
    data = re.sub(r"[^a-zA-z0-9]","",text).lower()
    if data==data[::-1]:
        return True
    else:
        return False
# print(palindrome(text))

lst = [1,2,1,1,1,2,3,4,5,6,2,3,4]

duplicates = [i for i in set(lst) if lst.count(i)>1]
# print(duplicates)
# ----------------------------------------------------------------
def fi(n):
    fib = [0,1]
    for i in range(n):
        fib.append(fib[-1]+fib[-2])
    return fib
#print(fi(10))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
# print(factorial(5))
# ----------------------------------------------------------
def first_non_repeating(s):
    freq = [0] * 26

    # Count frequency
    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    # Find first non-repeating
    for ch in s:
        if freq[ord(ch) - ord('a')] == 1:
            return ch

    return -1

# Example
# print(first_non_repeating("racecar"))

#--------------------------------------------------------------
def longestPalindrome(s):
    if len(s) < 1:
        return ""

    start = 0
    end = 0
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # actual palindrome length

    for i in range(len(s)):
        len1 = expand(i, i)      # odd length # center is single character  #aba
        len2 = expand(i, i + 1)  # even length #center is between two characters #abba
        max_len = max(len1, len2)

        if max_len > end - start: #check we found longest palindrome before
            start = i - (max_len - 1) // 2  #calculate where palindrome begins
            end = i + max_len // 2 #calculate where palindrome ends
    return s[start:end+1] # slicing from start to end include
print(longestPalindrome("babad"))

# ------------------------------------------------

def outer():
    cache = {}
    def inner(func):
        def wrapper(n):
            if n in cache:
                return cache[n]
            result = func(n)
            cache[n] = result
            return result
        return wrapper
    return inner


@outer()
def calling(n):
    if n<=1:
        return n
    return calling(n-1) + calling(n-2)
print(calling(10))
# -------------------------------------------------------------
import asyncio
import time

async def bad_async(name:str):
    print(f"{name}")
    time.sleep(1)
    print(f"{name}")


async def main():
    start = time.time()
    await asyncio.gather(bad_async('A'),bad_async('B'),)
    print(time.time() - start)

if __name__ == "__main__":
    asyncio.run(main())
# ---------------------------------------------------------------
# s = "aabcccccaaa"
#
# result = ""
# count = 1
#
# for i in range(1, len(s)):
#     if s[i] == s[i-1]:
#         count += 1
#     else:
#         result += s[i-1] + str(count)
#         count = 1
#
# # add last character
# result += s[-1] + str(count)
#
# # print(result)
# --------------------------------------------------------------
# def sum_of(num,target):
#     numbers = {}
#     for i,j in enumerate(num):
#         com = target - j
#         if com in numbers:
#             return [numbers[com],i]
#
#         numbers[j]=i
#
# # nums = [2, 7, 11, 15]
# # target = 18
# # print(sum_of(nums, target))
#
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [nums[i], nums[j]]
#
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))

# Here are some important Python coding questions on maximum length of subarray / substring, along with clear explanations and code. These are very common in interviews.
#
# 🔹 1. Maximum Length Subarray with Sum = K
# Problem:
#
# Given an array of integers, find the maximum length of a subarray whose sum equals K.
#
# ✅ Efficient Approach (Prefix Sum + HashMap)
# def max_len_subarray_sum_k(arr, k):
#     prefix_sum = 0
#     max_len = 0
#     seen = {}  # stores prefix_sum: index
#
#     for i in range(len(arr)):
#         prefix_sum += arr[i]
#
#         if prefix_sum == k:
#             max_len = i + 1
#
#         if prefix_sum - k in seen:
#             max_len = max(max_len, i - seen[prefix_sum - k])
#
#         if prefix_sum not in seen:
#             seen[prefix_sum] = i
#
#     return max_len
#
# # Example
# print(max_len_subarray_sum_k([1, -1, 5, -2, 3], 3))  # Output: 4
# 🔹 2. Longest Subarray with Equal 0s and 1s
# Problem:
#
# Find the largest subarray with equal number of 0s and 1s.
#
# ✅ Trick:
#
# Convert 0 → -1, then solve like sum = 0 problem.
#
# def longest_equal_0_1(arr):
#     prefix_sum = 0
#     max_len = 0
#     seen = {0: -1}
#
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             prefix_sum += -1
#         else:
#             prefix_sum += 1
#
#         if prefix_sum in seen:
#             max_len = max(max_len, i - seen[prefix_sum])
#         else:
#             seen[prefix_sum] = i
#
#     return max_len
#
# # Example
# print(longest_equal_0_1([0,1,0,1,1,1,0]))  # Output: 6
# 🔹 3. Longest Subarray with At Most K Distinct Elements
# Problem:
#
# Find max length subarray with at most K distinct numbers.
#
# ✅ Sliding Window
# from collections import defaultdict
#
# def longest_k_distinct(arr, k):
#     left = 0
#     freq = defaultdict(int)
#     max_len = 0
#
#     for right in range(len(arr)):
#         freq[arr[right]] += 1
#
#         while len(freq) > k:
#             freq[arr[left]] -= 1
#             if freq[arr[left]] == 0:
#                 del freq[arr[left]]
#             left += 1
#
#         max_len = max(max_len, right - left + 1)
#
#     return max_len
#
# # Example
# print(longest_k_distinct([1,2,1,2,3], 2))  # Output: 4
# 🔹 4. Longest Substring Without Repeating Characters
# Problem:
#
# Classic string problem (variation of subarray).
#
# def longest_unique_substring(s):
#     char_set = set()
#     left = 0
#     max_len = 0
#
#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#
#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)
#
#     return max_len
#
# # Example
# print(longest_unique_substring("abcabcbb"))  # Output: 3
# 🔹 5. Maximum Length Subarray with Sum ≤ K
# Problem:
#
# Find longest subarray with sum less than or equal to K.
#
# ✅ Sliding Window (for positive numbers only)
# def max_len_sum_le_k(arr, k):
#     left = 0
#     curr_sum = 0
#     max_len = 0
#
#     for right in range(len(arr)):
#         curr_sum += arr[right]
#
#         while curr_sum > k:
#             curr_sum -= arr[left]
#             left += 1
#
#         max_len = max(max_len, right - left + 1)
#
#     return max_len
#
# # Example
# print(max_len_sum_le_k([1,2,1,0,1,1,0], 4))  # Output: 5
# 🔹 6. Longest Subarray of 1s After Replacing K Zeros
# Problem:
#
# Flip at most K zeros → maximize consecutive 1s.
#
# def longest_ones(arr, k):
#     left = 0
#     zeros = 0
#     max_len = 0
#
#     for right in range(len(arr)):
#         if arr[right] == 0:
#             zeros += 1
#
#         while zeros > k:
#             if arr[left] == 0:
#                 zeros -= 1
#             left += 1
#
#         max_len = max(max_len, right - left + 1)
#
#     return max_len
#
# # Example
# print(longest_ones([1,1,0,0,1,1,1,0], 2))  # Output: 7
# 🔥 Key Patterns You Should Remember
#
# Most max-length subarray problems fall into:
#
# ✅ 1. Prefix Sum + HashMap
# Used when:
# Sum = K
# Equal counts
# Works with negative numbers
# ✅ 2. Sliding Window
# Used when:
# Positive numbers
# "At most K"
# "No duplicates"
# Faster and simpler
# 💡 Interview Tip
#
# If you see:
#
# "exact sum" → Prefix sum
# "at most / no repeating" → Sliding window
# ---------------------------------------------------------------------
# def maxLenSubarray(arr, k):
#     prefix_sum = 0
#     max_len = 0
#     prefix_map = {}
#
#     for i in range(len(arr)):
#         prefix_sum += arr[i]
#
#         if prefix_sum == k:
#             max_len = i + 1
#
#         if (prefix_sum - k) in prefix_map:
#             max_len = max(max_len, i - prefix_map[prefix_sum - k])
#
#         if prefix_sum not in prefix_map:
#             prefix_map[prefix_sum] = i
#
#     return max_len
#
#
# arr = [6,5,2,1,3,6]
# k = 6
# print(maxLenSubarray(arr, k))


#Decorators and use cases in production systems
# 1.Decorators are implement ->> Aspect-oriented-programming(AOP) style behavior
#2. They allow you to inject behavior around function calls without modifying the function itself.
# Decorator resolves typical production concerns:
    #logging - Centralized instrumentation
    #Authentication/Authorization - Security Enforcement
    #Retry logic - Resilience
    #Rate Limiting - API Protection
    #Caching - Performance
    #Metrics - Observability
    #Validation - Input Contracts
    #Feature flags - Controlled rollout

    #Instead of polluting business logic with infrastructure code ,decorators separate concerns cleanly.
# import time
# from functools import wraps
# import logging
#
# logging = logging.getLogger(__name__)
#
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         logging.info(f"{func.__name__}")
#         try:
#             return func(*args,**kwargs)
#         finally:
#             duration = time.time() - start
#             logging.info(f"{func.__name__},duration:{duration}")
#
#     return wrapper
#
# @decorator
# def sum_of(a,b):
#     return a+b
# print(sum_of(5,7))


# Context Manager?
# 1.Context manager controls resource lifecycle
# def file_opening():
#     with open("sample.txt","r") as f:
#         read = f.read()
#         print(read)

# print(file_opening())

# Context Manager solves

# files  - >> descriptor leaks
# DB connections  ->> pool exhaustion
#locks ->>deadlocks
#network sockets ->> resource leak
#trasanctions ->> partial commits

# context managers guarantee deterministic cleanup
#
# class Transaction:
#
#     def __enter__(self,db):
#         db.begin()
#
#     def __exit__(self,db,exc_type,exc,traceback):
#         if exc:
#             db.rollbck()
#         else:
#             db.commit()

# prevents in consistent data
# automatic rollback


# Production Benefits
#
# • Consistent logging
# • No duplicate boilerplate
# • Easy instrumentation across services
#
# Frameworks like FastAPI, Flask, Django internally rely on this pattern.
#
# Production Use Case 2 — Retry Logic
#
# Common in microservices and distributed systems.
#
# import time
# from functools import wraps
#
# def retry(attempts=3, delay=1):
#
#     def decorator(func):
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#
#             for attempt in range(attempts):
#                 try:
#                     return func(*args, **kwargs)
#
#                 except Exception as e:
#                     if attempt == attempts - 1:
#                         raise
#
#                     time.sleep(delay)
#
#         return wrapper
#
#     return decorator
#
# Usage:
#
# @retry(attempts=5, delay=2)
# def call_payment_service():
#     ...
# Production Benefit
#
# Handles:
#
# • transient network failures
# • service unavailability
# • flaky APIs
#
# Libraries like tenacity use this exact concept.
#
# Production Use Case 3 — Authentication / Authorization
#
# Widely used in web frameworks.
#
# Example:
#
# def require_admin(func):
#
#     @wraps(func)
#     def wrapper(user, *args, **kwargs):
#
#         if not user.is_admin:
#             raise PermissionError("Admin required")
#
#         return func(user, *args, **kwargs)
#
#     return wrapper
#
# Usage:
#
# @require_admin
# def delete_user(user, user_id):
#     ...
#
# Production advantages:
#
# • Security policy centralized
# • Easy enforcement across endpoints
#
# Production Use Case 4 — Caching
#
# Used in performance-critical workloads.
#
# Python provides built-in decorator:
#
# from functools import lru_cache
#
# @lru_cache(maxsize=1000)
# def expensive_calculation(x):
#     ...
#
# Production use:
#
# • ML feature computation
# • configuration lookup
# • metadata fetches
#
# Decorators in Major Frameworks
# Framework	Example
# Flask	@app.route()
# FastAPI	@app.get()
# Django	@login_required
# Celery	@shared_task
# PyTest	@pytest.fixture
#
# Example from FastAPI:
#
# @app.get("/users")
# def get_users():
#     ...
#
# @app.get registers route metadata via decorator.
#
# Advanced Decorator Patterns
# 1. Class Decorators
#
# Used to modify class behavior.
#
# Example:
#
# def singleton(cls):
#
#     instances = {}
#
#     def get_instance(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return get_instance
#
# Usage:
#
# @singleton
# class DBConnection:
#     pass
# 2. Stacked Decorators
#
# Multiple concerns applied sequentially.
#
# @retry()
# @log_execution
# @metrics
# def fetch_data():
#     ...
#
# Execution order:
#
# metrics(log_execution(retry(fetch_data)))
# Pitfalls with Decorators
# 1. Lost function metadata
#
# Fix:
#
# from functools import wraps
# 2. Debugging complexity
#
# Stack traces can become harder.
#
# 3. Hidden side effects
#
# Too many decorators → unreadable behavior.

# 1.5 Rate Limiting / Circuit Breaking

# Decorators can implement:
#
# rate limiting
#
# circuit breakers
#
# request throttling
#
# These are common in API gateways and microservices.
# Benefits
#
# Guarantees rollback on failure
#
# Avoids forgotten commits
#
# Clean transactional boundaries
#
# Used in:
#
# SQLAlchemy
#
# Django ORM
#
# internal database libraries

# from functools import lru_cache,wraps
#
# def decorator(retry=3,delay=1):
#     def inside_decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             for i in range(retry):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                    if i == retry -1:
#                        raise
#                 time.sleep(delay)
#
# @decorator(retry=3,delay=1)
# def session_call(a,b):
#     return a+b
#
# session_call(10,20)





###2. Context Managers in Production Systems

# Context managers control resource lifecycle.
#
# Typical pattern:
#
# with resource() as r:
#     use(r)
#
# Equivalent to:
#
# setup
# try:
#    block
# finally:
#    cleanup
# Problem Context Managers Solve
#
# Production code frequently deals with:
#
# Resource	Risk
# Files	descriptor leaks
# DB connections	pool exhaustion
# Locks	deadlocks
# network sockets	resource leak
# transactions	partial commits
#
# Context managers guarantee deterministic cleanup.
#
# Basic Context Manager Example
# with open("file.txt") as f:
#     data = f.read()
#
# Equivalent:
#
# f = open("file.txt")
# try:
#     data = f.read()
# finally:
#     f.close()
# Production Use Case 1 — Database Transactions
#
# Example:
#
# with db.transaction():
#     create_order()
#     charge_payment()
#
# Implementation:
#
# class Transaction:
#
#     def __enter__(self):
#         db.begin()
#
#     def __exit__(self, exc_type, exc, tb):
#         if exc:
#             db.rollback()
#         else:
#             db.commit()
#
# Production benefit:
#
# • prevents inconsistent data
# • automatic rollback on error
#
# Production Use Case 2 — Locks / Concurrency
#
# Thread safety:
#
# from threading import Lock
#
# lock = Lock()
#
# with lock:
#     critical_section()
#
# Equivalent manual code:
#
# lock.acquire()
# try:
#     ...
# finally:
#     lock.release()
#
# Used heavily in:
#
# • multi-threaded services
# • schedulers
# • caches
#
# Production Use Case 3 — Temporary Configuration
#
# Example:
#
# with set_env("DEBUG", "true"):
#     run_tests()
#
# Custom context manager:
#
# import os
#
# class set_env:
#
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#
#     def __enter__(self):
#         self.old = os.getenv(self.key)
#         os.environ[self.key] = self.value
#
#     def __exit__(self, *args):
#         if self.old:
#             os.environ[self.key] = self.old
# Production Use Case 4 — Performance Timing
# with timer("data_load"):
#     load_data()
# Context Managers Using contextlib
#
# Python provides a simpler approach.
#
# from contextlib import contextmanager
#
# @contextmanager
# def timer(name):
#
#     start = time.time()
#     yield
#     print(name, time.time() - start)
#
# Usage:
#
# with timer("task"):
#     process()
# Decorators vs Context Managers
# Aspect	Decorator	Context Manager
# Scope	Entire function	Block of code
# Syntax	@decorator	with
# Use Case	Cross-cutting function behavior	Resource lifecycle
# Control	Function invocation	Code block execution
#
# Example difference:
#
# Decorator:
#
# @retry
# def call_api():
#
# Context manager:
#
# with retry_context():
#     call_api()
# When To Use Each (Production Decision)
#
# Use decorators when:
#
# • behavior applies to function boundaries
# • used across many functions
# • enforcing policies
#
# Examples:
#
# authentication
#
# caching
#
# retries
#
# metrics
#
# Use context managers when:
#
# • controlling resource lifetime
# • code block specific behavior
#
# Examples:
#
# transactions
#
# locks
#
# files
#
# temporary state
#
# Combining Both (Advanced Pattern)
#
# Example in production frameworks.
#
# Decorator:
#
# @transactional
# def create_order():
#
# Inside implementation:
#
# with db.transaction():
#
# Decorator provides API, context manager handles resource management.
#
# Real Production Architecture Example
#
# Example microservice stack:
#
# @metrics
# @retry
# @timeout
# @auth_required
# def process_order():
#
# Inside:
#
# with db.transaction():
#     update_inventory()
#     charge_payment()
#
# Benefits:
#
# • clean business logic
# • centralized cross-cutting concerns
# • safe resource management
#
# Design Advice for Tech Leads
# 1. Limit decorator depth
#
# Too many decorators create invisible behavior.
#
# Rule of thumb:
#
# <= 3 decorators
# 2. Always preserve metadata
#
# Use:
#
# @wraps(func)
# 3. Keep decorators pure
#
# Avoid:
#
# global state mutation
# 4. Prefer context managers for resources
#
# Never hide resource control in decorators.
#
# Summary
# Concept	Key Role
# Decorators	Inject behavior around functions
# Context Managers	Manage resource lifecycle
# Decorators	Cross-cutting concerns
# Context Managers	Deterministic cleanup
#
# Production systems rely on both to achieve:
#
# • clean architecture
# • reusability
# • fault tolerance
# • observability
#
# If you'd like, I can also explain 3 advanced topics that senior engineers are often asked in staff/principal interviews:
#
# 1️⃣ How FastAPI and Flask internally implement decorators
# 2️⃣ Building distributed tracing decorators (OpenTelemetry)
# 3️⃣ Async context managers and async decorators in modern Python systems
#
# These are very common Staff Engineer interview topics. 🚀



# from contextlib import contextmanager
#
#
# @contextmanager
# def transaction(session):
#     try:
#         yield session
#         session.commit()
#     finally:
#         session.rollback()
#         session.close()

# Production examples:

    # database connections
    #
    # Redis clients
    #
    # Kafka producers
    #
    # thread locks
    #
    # temporary directories

# Use decorators when behavior belongs to the function.
# Use context managers when behavior belongs to a specific block of work.

from itertools import combinations
#
input = [["E1","ProjectA"],
         ["E2","ProjectB"],
         ["E1","ProjectB"],
         ["E3","ProjectA"],
         ["E2","ProjectA"]]


# emp_projects ={}
# for key,value in input:
#     if value in emp_projects:
#         emp_projects[key].append(value)
#     else:
#         emp_projects[key]=[value]
# print(emp_projects)
emp_projects = {}
for emp, proj in input:
    emp_projects.setdefault(emp, []).append(proj)


result = {}

for e1, e2 in combinations(emp_projects.keys(),2):
    common = list(set(emp_projects[e1]) & set(emp_projects[e2]))
    if common:
        result[f"{e1},{e2}"] = common

# print(result)
# data = [
#   ["C1", "Laptop"],
#   ["C2", "Phone"],
#   ["C1", "Phone"],
#   ["C3", "Laptop"],
#   ["C2", "Laptop"]
# ]
#
# # Step 1: customer -> products
# customer_products = {}
#
# for customer, product in data:
#     customer_products.setdefault(customer, set()).add(product)
#
# # Step 2 & 3: compare customer pairs
# result = {}
#
# for c1, c2 in combinations(customer_products.keys(), 2):
#     common_products = list(customer_products[c1] & customer_products[c2])
#     if common_products:
#         result[f"{c1},{c2}"] = common_products
#
# print(result)
# Example Input:
# lst = [1, 3, 4, 2, 2,3,3,4,6,5]
# seen = set()
# s=[]
# for i in lst:
#     if i not in seen:
#         seen.add(i)
#     else:
#         s.append(i)
# print(seen)
# print(s)

import re
text  ="kik"

def palindrome(text):
    data = re.sub(r"[^a-zA-z0-9]","",text).lower()
    if data==data[::-1]:
        return True
    else:
        return False
# print(palindrome(text))

lst = [1,2,1,1,1,2,3,4,5,6,2,3,4]

duplicates = [i for i in set(lst) if lst.count(i)>1]
# print(duplicates)

def fi(n):
    fib = [0,1]
    for i in range(n):
        fib.append(fib[-1]+fib[-2])
    return fib
#print(fi(10))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
# print(factorial(5))

def first_non_repeating(s):
    freq = [0] * 26

    # Count frequency
    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    # Find first non-repeating
    for ch in s:
        if freq[ord(ch) - ord('a')] == 1:
            return ch

    return -1

# Example
# print(first_non_repeating("racecar"))

#
def longestPalindrome(s):
    if len(s) < 1:
        return ""

    start = 0
    end = 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # actual palindrome length

    for i in range(len(s)):
        len1 = expand(i, i)      # odd length # center is single character  #aba
        len2 = expand(i, i + 1)  # even length #center is between two characters #abba
        max_len = max(len1, len2)

        if max_len > end - start: #check we found longest palindrome before
            start = i - (max_len - 1) // 2  #calculate where palindrome begins
            end = i + max_len // 2 #calculate where palindrome ends

    return s[start:end+1] # slicing from start to end include


# Example
print(longestPalindrome("babad"))


def outer():
    cache = {}
    def inner(func):
        def wrapper(n):
            if n in cache:
                return cache[n]
            result = func(n)
            cache[n] = result
            return result
        return wrapper
    return inner


@outer()
def calling(n):
    if n<=1:
        return n
    return calling(n-1) + calling(n-2)
print(calling(10))