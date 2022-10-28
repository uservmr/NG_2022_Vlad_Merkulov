def fun(cnt):
    x=0
    for i in s:
        if i == cnt:
            x+=1
    print(cnt,x)
s = str(input('Ведіть символи: '))
print("Number of letters in a string", len(s))
print("Number of each letter separately: ")
for cnt in s:
    fun(cnt)
print("Sorted by letters: ")
for cnt in sorted(s):
    fun(cnt)