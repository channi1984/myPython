number = input("정수 입력>")
number = int(number)

#양수 조건
if number > 0:
	print("양수입니다")

#음수 조건
if number < 0:
	print("음수입니다.")

# 0 조건
if number == 0:
	print("0입니다.")

i = 0
while i <= 10:
	print(i)
	i+=1

sum = 0
for i in range(11):
	sum += i
print(sum)

list = ["This", "is", "a", "book"]
for s in list:
	print(s)

numbers = range(2,11,2)

for x in numbers:
	print(x)

a = ["AB", 0, False]
a.append(21.5)
a[1] = 11
del a[2]
print(a)

a= [1,2]
b= [3,4,5]
c= a+b
print(c)
d= a*3
print(d)

mylist = "This is a book That is pencil".split()
i = mylist.index('book')
n = mylist.count('is')
print(i,n)

scores = {"철수":90, "민수":80, "영희":80}
v = scores["민수"]
scores["민수"] = 88
print(v)

scores = {"철수":90, "민수":80, "영희":80}
for key in scores:
	val = scores[key]
	print(key, val)


myset = {1,1,3,5,5}
print(myset)

mylist = ["A","A","B","B","B",]
s = set(mylist)
print(s)


myset = {1,3,5}

myset.add(7)
print(myset)

myset.update({4,2,10})
print(myset)

myset.remove(1)
print(myset)

myset.clear()
print(myset)


a = {1, 3, 5}
b = {1, 2, 5}

i = a & b
print(i)

u = a | b
print(u)

d = a - b
print(d)

def sum(a,b):
	s = a+b
	return s
total = sum(4,6)
print(total)

def clac(i,j,factor=1):
	return i*j*factor

result = clac(10,20)

print(result)

def total(*numbers):
	tot = 0
	for n in numbers:
		tot+=n
	return tot

t = total(1,2)
print(t)
t = total(1,4,2,6)
print(t)

class Rectangle:
	count = 0

	def __init__(self, width, height) :
		self.width = width
		self.height = height
		Rectangle.count += 1

	def calcArea(self):
		area = self.width * self.height
		return area

import random

rn = ["0", "0", "0"]
rn[0] = str(random.randrange(1, 9, 1))
rn[1] = rn[0]
rn[2] = rn[0]

while (rn[0] == rn[1]):
    rn[1] = str(random.randrange(1, 9, 1))
while (rn[0] == rn[2] or rn[1] == rn[2]):
    rn[2] = str(random.randrange(1, 9, 1))

# print(rn)

t_cnt = 0
s_cnt = 0
b_cnt = 0

print("숫자야구게임을 시작합니다!!!")
print("---------------------")

while (s_cnt < 3):
    num = str(input("숫자 3자리를 입력하세요:"))

    s_snt = 0
    b_scnt = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if(num[i] == str(rn[j]) and i == j):
                s_cnt += 1
            elif(num[i] == str(rn[j]) and i != j):
                b_cnt = +1
    print("결과 : [", s_cnt, "] Strike[", b_cnt, "] Ball")
    t_cnt += 1

print("--------------------")
print(t_cnt, "번 만에 정답을 맞추셨습니다.")

var_string = 'Life is Short! You Need Python!!'

print(var_string[0])
print(var_string[24])

print(var_string[-1])

print(var_string[-32])
print(var_string[-8])

var_str = 'PYTHON'

print(var_str[0:3])
print(var_str[2:5])
print(var_str[2:])
print(var_str[:3])

print(var_str[-6:-3])
print(var_str[-4:-1])
print(var_str[-4:])
print(var_str[:-3])

var_str = 'Life is short! You need Pyton!!'

print(var_str.upper())
print(var_str.lower())
print(var_str.title())
print(var_str.swapcase())

print(var_str.count('e'))
print(var_str.find('Python'))

print(var_str.endswith('?'))
print(var_str.endswith('!'))
print(var_str.startswith('l'))
print(var_str.startswith('L'))
print(var_str.lower().startwith('l'))

var_list1 = var_str.split()
print(var_list1)
var_list2 = var_str.split('! ')
print(var_list2)

value = 2

if(value == 1):
    print("value One")

if(value == 2):
    print("value Two")

value = 2

if(value == 1):
    print("value One")
else:
    print("value Noe One ")

if(value == 2):
    print("value Two")
else:
    print("value Not Two")