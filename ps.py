'''
a = int(input("Enter number to create multiplication table : "))

for i in range(1, 11):
    print(str(i) + " * " + str(a) + " = " + str(i*a))



b = int(input("Enter number to do factorial : "))

result = 1
for i in range(1, b+1):
    result = result * i
print(result)



series = [0, 1]

c = int(input("Enter the size of fibonacci series"))

for i in range(2, c):
    series.append(series[i-1] + series[i-2])

print(series)



inp = int(input("Enter the number : "))
count = 0

while inp > 0:
    inp = inp // 10
    count += 1
print(count)
'''
