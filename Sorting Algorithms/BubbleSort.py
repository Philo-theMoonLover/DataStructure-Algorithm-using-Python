import random

random.seed(5)
array = []
for i in range(10):
    array.append(random.randint(-10, 10))
print('Array:', array)

for i in range(10):
    for j in range(10 - 1 - i):
        if array[j] > array[j + 1]:
            temp = array[j + 1]
            array[j + 1] = array[j]
            array[j] = temp
print('Array after sort:', array)

n = int(input("Enter number to search: "))
flag = False

while not flag:
    for i in range(len(array)):
        if array[i] == n:
            print("index = ", i)
            flag = True
    if not flag:
        print("Not found!")
        break
