# Problem Set 0
# Name: A C
# Collaborators: none
# Time Spent: 3:30

x = int(raw_input("Enter integer: "))
epsilon = 0.01
a = 0.0
i = 0

# loop until find cube root or pass input
while abs(a**2 - x) >= epsilon and a <= x:
    a += 0.00001
    i += 1

print "Iterations: ", i

if abs(a**2 - x) >= epsilon:
    print "Failed on square root of", x
else:
    print a, "is close to the square root of", x
