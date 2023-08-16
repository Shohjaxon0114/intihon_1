# 1. 2 ta  qatorning har birida  yosh va ismlarni
# qabul qilib, ulardan yoshi kichigini ismini chiqarish
# dasturinintuzing.
try:
    a = list(input().split(' '))
    b = list(input().split(' '))
    if int(a[0])<int(b[0]):
        print(a[1])
    else:
        print(b[1])
except ValueError:
    print('1-yosh yozin 2-isim yozin')
