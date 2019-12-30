from random import randint
from math import sqrt
def play():
   a=100
   b=200
   print(hex(a))
   print(hex(b))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
def quadratic(a, b, c):
    delta=b*b-4*a*c
    if delta>0:
        return (-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)
    elif delta==0:
        return (-b)/2*a
    elif delta<0:
        return None
def product(*args):
    if len(args)==0:
        raise TypeError('请至少输入一个参数！')
    sum=1
    for n in args:
        sum=sum*n
    return sum
def hanoi(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        hanoi(n-1,a,c,b)
        print(a,'-->',c)
        hanoi(n-1,b,a,c)
def trim(s):
    if len(s)==0:
        return s
    n=0
    while ord(s[n])==32:
        n=n+1
    s=s[n:]
    m=len(s)
    while ord(s[m-1])==32:
        m=m-1
    s=s[:m]
    return s




if __name__=="__main__":
    s="   abc"
    print(len(s))
    print(trim(s))
    print(len(s))

    # play()
    # print(my_abs('sg'))
    # print(my_abs(10))
    # print(my_abs(-10))
    # print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
    # print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
    #
    # if quadratic(2, 3, 1) != (-0.5, -1.0):
    #     print('测试失败')
    # elif quadratic(1, 3, -4) != (1.0, -4.0):
    #     print('测试失败')
    # else:
    #     print('测试成功')
    # print(product())
    # 测试
    # print('product(5) =', product(5))
    # print('product(5, 6) =', product(5, 6))
    # print('product(5, 6, 7) =', product(5, 6, 7))
    # print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
    # if product(5) != 5:
    #     print('测试失败!')
    # elif product(5, 6) != 30:
    #     print('测试失败!')
    # elif product(5, 6, 7) != 210:
    #     print('测试失败!')
    # elif product(5, 6, 7, 9) != 1890:
    #     print('测试失败!')
    # else:
    #     try:
    #         product()
    #         print('测试失败!')
    #     except TypeError:
    #         print('测试成功!')
    # hanoi(6,'a','b','c')
