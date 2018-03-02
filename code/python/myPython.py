# *-* coding:utf-8 *-*

from functools import partial


# 可读性好

# range()

print range(0,9,2) #递增列表

for i in xrange(0,9,2): # 只用于for 循环中
	print i

albums = ("Poe","Gaudi","Freud","Poe2")
years = (1976,1987,1990,2003)
for album in sorted(albums):
	print album

for album in reversed(albums):
	print album

for i,album in enumerate(albums):
	print i,album

for album,yr in zip(albums,years):
	print album,yr


# 列表表达式
# 8.12 列表解析，列表解析的表达式比map lambda效率更高

def fuc(a):
	return a**2

x = range(1,10,1)
print x
print map(fuc,x)
# map 对所有的列表元素执行一个操作
# lambda 创建只有一行的函数 -- 只使用一次，非公用的函数
print map(lambda x:x**2,range(6))

print [x**2 for x in range(6) if x>3]

print filter(lambda x:x%2,range(10))
print [x for x in range(10) if x%2]


# 11.7.2 函数式编程

print range(6)  
print reduce(lambda x,y:x+y,range(6)) # 累加

# 偏函数   简化代码，提高代码速度

int2 = partial(int,base=2)
print int2('1000')
# 闭包


# 列表生成器

g = (x for x in range(10))
print g.next()
print "------"
for n in g:
	print n

# 匿名函数，无函数名，将函数赋给变量
f = lambda x:x*x
print f(2)

# 装饰器
def log():
	print 'log'



def now():
	print 'time is:','2017-09-14'



# 字典




