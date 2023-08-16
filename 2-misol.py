# 2. 1 ta qatorda kiritiladigan bir nechta so’zlardagi katta harflarni
# list ko’rinishida va ularning sonini chiqaring.\

try:
    a=list(input())
    b=[ ]
    s=0
    for i in a:
        if 65<=ord(i)<90:
            b.append(str(i))
            s+=1
    print(b,'\n',s)
except ValueError:
    print(' ')