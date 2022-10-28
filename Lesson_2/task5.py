list1 = list(map(int,input('Enter price values separated by a space: ').split()))
print(list1)
max = list1[0]
min = list1[0]
sum = 0
for i in range(1, len(list1)):
    if (list1[i] > max):
        max = list1[i]
print("Maximum value:", max)
for i in range(1, len(list1)):
    if (list1[i] < min):
        min = list1[i]
print("Minimum value:", min)
for i in range(0, len(list1)):
        sum = sum + list1[i] 
sum = sum - (max + min)       
print("The sum of the remaining elements:", sum)

