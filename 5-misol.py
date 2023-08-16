# 5. 2 ta turli qatorda sonlar vergul orqali ajratib beriladi.
# Faqatgina 1-qatorda yoki faqatgina 2-qatorda bor sonlarni
# kamayish tartibida chiqaring. Natijada dublikat qiymatlar bo’lmasin!

a = set(input().split(','))
b = set(input().split(','))
c = list(a.union(b)-a.intersection(b))
l = str("")
for i in c:
    l = i + ' ' + l
l = l[:-1]
print(l)
