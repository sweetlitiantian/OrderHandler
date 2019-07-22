#!/user/bin/python
# -*- coding: UTF-8 -*-
import random
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i!= k)and(i != j)and(j != k):
#                 print i,j,k
#
#
# l = []
# for i in range(3):
#     x = int(raw_input('integer:\n'))
#     l.append(x)
# l.sort()
# print l
# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b,a+b
#     return a
# print fib(10)
#
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# print fib(10)

#
# import time
#
# myD = {1:'a',2:'b'}
# for key,value in dict.items(myD):
#     print key,value
#     time.sleep(1)

# h = 0
# leap = 1
# from math import sqrt
# from sys import stdout
# for m in range(101,201):
#     k = int(sqrt(m+1))
#     for i in range(2,k+1):
#         if m%i == 0:
#             leap = 0
#             break
#     if leap == 1:
#         print '%-4d'%m
#         h+=1
#         if h%10 == 0:
#             print ''
#     leap = 1
# print 'the total is %d'%h


# a = int(raw_input("请输入一个数:\n"))
# x = str(a)
# flag = True
# for i in range(len(x)/2):
#     if x[i] != x[-i-1]:
#         flag = False
#         break
# if flag:
#     print "%d是一个回文数"%a
# else:
#     print"%d 不是一个回文" %a

# letter = raw_input("please input:")
# # if letter == 'S':
# #     print('please input second letter:')
# #     letter = raw_input("please input:")
# #     if letter =='a':
# #         print ('Staturday')
# #     elif letter == 'u':
# #         print('Sunday')
# #     else:
# #         print('data error')
# # elif letter =='F':
# #     print('Friday')
# # elif letter == 'W':
# #     print('Wenesday')
# # elif letter =='T':
# #     print('please input second')
# #     letter = raw_input("please input:")
# #     if letter == 'u':
# #         print('Tuesday')
# #     elif letter =='h':
# #         print('Thursday')
# #     else:
# #         print('data error')
# # elif letter =='W':
# #     print('Wednesday')
# # else:
# #     print('data error')


# L = [1,2,3,4,5]
# s1 = ','.join(str(n) for n in L)
# print s1
#
# def hello_world():
#     print ('hello world')
#
#
# def three_hellos():
#     for i in range(3):
#         hello_world()
#
#
# if __name__ == '__main__':
#     three_hellos()
# lower = int(input("请输入区间最小值"))
# upper  = int(input("请输入区间最大值"))
#
# for num in range(lower,upper + 1):
#     if num >1:
#         for i in range(2,num):
#             if(num % i) == 0:
#                 break
#         else:
#             print(num)
# 冒泡排序
# def bubble_sort(data):
#     for i in  range(len(data) -1):
#         indicator = False
#         for j in range(len(data)-1-i):
#             if data[j]>data[j+1]:
#                 data[j],data[j+1] = data[j+1],data[j]
#                 indicator = True
#         if not indicator:
#             break
# data = list(range(10))
# random.shuffle(data)
#
# print(data);
# bubble_sort(data)
# print(data)
#
# def bubble_sort(data):
#     for i in range(len(data)-1):
#         indicator = False
#         for j in range(len(data)-1-i):
#             if data[j] > data[j+1]:
#                 data[j],data[j+1] = data[j+1],data[j]
#                 indicator = True
#         if not indicator:
#             break
# data = list(range(10))
# random.shuffle(data)
# print(data);
# bubble_sort(data)
# print(data)

if __name__ =="__main__":
    N=10
    print '请输入10个数字:\n'
    l = []
    for i in range(N):
        l.append(int(raw_input('请输入一个数字：\n')))
    print
    for i in range(N):
        print l[i]
        #排列10个数字
    for i in range(N-1):
        min = i
        for j  in  range(i+1,N):
            if l[min] >l[j]:min = j
        l[i],l[min] = l[min],l[i]
        print '排列之后:'
        for i in range(N):
            print l[i]
