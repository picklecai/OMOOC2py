# _*_ coding: utf-8 _*_
# 给程序员的超快速指南
import os
def main():
    print "Hello world!"
    print '这是Bob \'的问候。'

    foo(5, 10)

    print '=' *10
    print '这将直接执行' + os.getcwd()

    counter = 0
    counter += 1

    food=['苹果','杏子','李子','梨']
    for i in food:
        print '俺就爱整只'+i

    print '数到10'
    for i in range(10):
        print i 

def foo(param1, secondparam):
    res= param1 + secondparam
    print '%s 加 %s 等于 %s' %(param1, secondparam, res)
    if res <50:
        print'这个'
    elif (res >=50) and ((param1==42) or (secondparam==24)):
        print '那个'
    else:
        print '嗯...'
    return res #这是单行注释
    '''这是多
行注释……'''

if __name__=='__main__':
    main() 
