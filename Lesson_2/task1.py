def fun(letters):
    numberofletters=0
    for indexofletters in string:
        if indexofletters == letters:
            numberofletters+=1
    print(letters,numberofletters)
string = str(input('Enter the string: '))
print("Number of letters in a string:", len(string))
print("Number of each letter separately: ")
for letters in string:
    fun(letters)
print("Sorted by letters: ")
for letters in sorted(string):
    fun(letters)