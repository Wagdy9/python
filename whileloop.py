#while loops
i = 1
while i <= 10:
    print("i")
    i += 1
else:
    print("The condition is not true")
print("The loop has ended")

x = 1
while x <= 10:
    
    x += 1
    if x == 6:
        continue
    
    print(x)
print("The loop has ended")

y = 1
while y <= 10:
    
    y += 1
    if y == 6:
        break
    
    print(y)
print("The loop has ended")