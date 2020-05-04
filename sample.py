import datetime

now = datetime.datetime.now()

print(now.year, "년")
# 2020년

print(now.month, "월")
# 5월

print(now.day, "일")
# 4일

print(now.hour, "시")
# 13시

print(now.minute, "분")
# 4분

print(now.second, "초")
# 33초

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))
    # 현재 시각은 10시로 오전입니다!

if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))
    # 현재 시각은 13시로 오후입니다!

if 3 <= now.month <= 6:
    print("지금은 봄입니다")
elif 7 <= now.month <= 0:
    print("지금은 여름입니다")
else:
    print("지금의 계절에는 관심이 없습니다.")

#########################################################################

number = "32"

last_character = number[-1]

last_number = int(last_character)

print(last_number)
# 2

if last_number == 0 \
        or last_number == 2 \
        or last_number == 4 \
        or last_number == 6 \
        or last_number == 8:
    print("짝수입니다")
    # 짝수입니다


if last_character in "2468":
    print("짝수입니다")
    # 짝수입니다


if last_number % 2 == 0:
    print("짝수입니다")
    # 짝수입니다
else:
    print("홀수입니다")
    # 홀수입니다

#########################################################################

array = [273, 32, 104, "문자열", True, False]
print(array)
# [273, 32, 104, '문자열', True, False]

list_a = array[0]
print(list_a)
# 273

list_b = array[3]
print(list_b)
# 문자열

list_c = array[3][0]
print(list_c)
# 문

#########################################################################

array2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(array2[1])
# [4, 5, 6]
print(array2[1][1])
# 5

#########################################################################

array3 = [1, 2, 3]
array4 = [4, 5, 6]

array_join = array3+array4
print(array_join)
# [1, 2, 3, 4, 5, 6]

array_multiply = array3 * 2
print(array_multiply)
# [1, 2, 3, 1, 2, 3]

array_length = len(array_join)
print(array_length)
# 6

#########################################################################

array5 = [1, 2, 3]
array5.append(4)
print(array5)
# [1, 2, 3, 4]

array5.insert(0, 0)
print(array5)
# [0,1, 2, 3, 4]

#########################################################################

array6 = [1, 2, 3, 4, 5]
for element in array6:
    print(element)
    # 1
    # 2
    # 3
    # 4
    # 5

#########################################################################

diction1 = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕"],
    "origin": "필리핀"
}

print(diction1["name"])
# 7D 건조 망고

del diction1["ingredient"]
print(diction1)
# {'name': '7D 건조 망고', 'type': '당절임', 'origin': '필리핀'}

for key in diction1:
    print(diction1[key])
# 7D 건조 망고
# 당절임
# 필리핀

#########################################################################

print(list(range(0, 10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(5, 10)))
# [5, 6, 7, 8, 9]

print(list(range(5, 10, 2)))
# [5, 7, 9]

array7 = [1, 2, 3, 4, 5]
for i in range(len(array7)):
    print("{}번째 반복 : {}".format(i, array7[i]))
# 0번째 반복 : 1
# 1번째 반복 : 2
# 2번째 반복 : 3
# 3번째 반복 : 4
# 4번째 반복 : 5

#########################################################################

i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1

# 0번째 반복입니다.
# 1번째 반복입니다.
# 2번째 반복입니다.
# 3번째 반복입니다.
# 4번째 반복입니다.
# 5번째 반복입니다.
# 6번째 반복입니다.
# 7번째 반복입니다.
# 8번째 반복입니다.
# 9번째 반복입니다.

#########################################################################

numbers = [134, 3, 23, 432, 222]
print(min(numbers))
# 3
print(max(numbers))
# 432
print(sum(numbers))
# 814
