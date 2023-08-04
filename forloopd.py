for letter in "wagdy":
    print(letter)
for char in "wagdy":
    print(char)
Buddies = ["wagdy", "mohamed", "ali", "alaa", "winner"]
for Buddy in Buddies:
    print(Buddy)

for x in range(5):
    print(x)

for x in range (5, 20):
    print(x)

for y in range (3, 9):
    print(y)


print(len(Buddies))
print(len("Buddies"))
print(len("wagdy"))


for x in range (len(Buddies)):
    print(x)

for x in range (4):
    print(x)

for x in range (len(Buddies)):
    print(Buddies[x])

for index in range (10):
    if index % 2 == 0:
        print(index, " is an even number")
    else:
        print(index, " is an odd number")


for buddy in range (len(Buddies)):
    if Buddies[buddy] == "winner":
        print(buddy," is the winner")
    else:
        print(buddy," is not the winner")

