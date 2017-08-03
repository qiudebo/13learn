#!/usr/bin/python
# -*- coding: utf-8 -*-

import  numpy as np

if __name__ == '__main__':

    city = ['beijing','shanghai','tianjin']

    for i, c in enumerate(city):
        print (i,c)

    x = np.arange(1,10)
    y = np.arange(11,20)

    for a,b in zip(x,y):
        print (a,b)


    m = 1
    n =2
    m,n = n,m
    print ('After m=%d, n=%d'%(m,n))

    ages = {
        'Bob': 31,
        'John': 28
    }

    age =ages.get('Bob1','Unknow')
    print ('Bob is %s years old'%age)



    print('converting!')
    try:
        print(int('1'))
    except:
        print('Conversion is failed!')
    else:
        print('Conversion is successful!')
    finally:
        print('done!')

    with open('test.txt') as f:
        for line in f:
            print(line)


    s = 'a'
    alpa = ['b','c','d']
    for letter in alpa:
        if s == letter:
            print('Found')
            break
    else:
        print ('Not Found')