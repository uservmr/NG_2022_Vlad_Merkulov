sec = int(input("Enter number of seconds: "))
day = sec // 86400
sec %= 86400
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
print(day, ":", hour, ":", min, ":", sec)
   
