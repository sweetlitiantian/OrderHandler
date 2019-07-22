# -*- coding: UTF-8 -*-
# if __name__ =='__main__':
#     a = []
#     sum = 0.0
#     for i in range(3):
#         a.append([])
#         for j in range(3):
#             a[i].append(float(raw_input("input num:\n")))
#     for i in range(3):
#         sum += a[i][i]
#     print sum
#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print j,"*",i,"=",i*j,"",
#     print("")
import urllib2
web = urllib2.urlopen('http//www.baidu.com')
content = web.read()
print content