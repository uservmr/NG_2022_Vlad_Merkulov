x = int(input('Input size: '))
for i in range(x): 
  for j in range(x-i,0,-1): 
    print(j, end = " ") 
  print()                 
