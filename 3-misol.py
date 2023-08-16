# 3. Istalgan xonali natural son kiritiladi. Shu sonning barcha
#  4 raqamlarini 7 ga, 7 raqamlarini esa 4 ga  aylantirib o’ziga
# o’zlashtiring va chiqaring

try:
    a=list(input())
    for i in range(len(a)):
        if a[i]=='4':
            a[i]='7'
        elif a[i]=='7':
            a[i]='4'
    print(''.join(a))
except ValueError:
    print(' ')