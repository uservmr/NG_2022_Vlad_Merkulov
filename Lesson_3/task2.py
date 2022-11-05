def sort(string):
    return sorted(string)
def countofelements(string):
    return len(string)
def volwelsorconsonants(string):
    volwels = 0
    consonants = 0
    all_vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", "a", "e", "i", "o", "u", "y"]
    for letters in string:
        if (letters in all_vowels):
            volwels += 1
        else:
            consonants +=1
    return volwels or consonants
def breakremove(string):
    s = string.split()
    return ' '.join([line.strip() for line in s][::-1]).split()
def wordsnum(string):
    firstindex = int(input("Enter first index:"))
    secondindex = int(input("Enter first index:"))
    return string[firstindex:secondindex]
def string1(string):
    string = str(input("Enter a string again:"))
    return string
string = str(input("Enter a string:"))
func = print("Select function: \nSort the string - 1\nCount the number of elements - 2\nOutput only vowels or consonants - 3\nBreak by words and remove word from the end - 4\nPrint word by number - 5\nEnter the string again - 6\nCompletion of the program - 7")
print("==============================")
func = int(input("Choose a function:"))
if (func == 1):
    print(sort(string))
elif (func == 2):
    print(countofelements(string))
elif (func == 3):
    print(volwelsorconsonants(string))
elif (func == 4):
    print(breakremove(string))
elif (func == 5):
    print(wordsnum(string))
elif (func == 6):
    print(string1(string))
elif (func == 7):
    exit(1)