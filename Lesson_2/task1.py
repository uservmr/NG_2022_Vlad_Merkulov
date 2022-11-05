def fun(letters):
    numberofletters=0
    for i in s:
        if i == letters:
            numberofletters+=1
    print(letters,numberofletters)
s = str(input('Enter the string: '))
print("Number of letters in a string", len(s))
print("Number of each letter separately: ")
for letters in s:
    fun(letters)
print("Sorted by letters: ")
for letters in sorted(s):
    fun(letters)