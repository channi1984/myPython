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


number = 42

last_character = number[-1]
print(last_character)
