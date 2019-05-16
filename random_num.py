print("RANDOM NUMBERS AND THEIR MEAN\n")
import random
arr=[]
for i in range(100):
    arr.append(random.randint(110,1000))
for num in arr:
    print(num)
print("=============================")
print("Sum of Numbers= ",sum(arr))
x=sum(arr)/9
print("Mean of Number= ", x)
    
