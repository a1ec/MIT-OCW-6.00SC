# Problem Set 0
# Name: A C
# Collaborators: none
# Time Spent: 3:30

x = int(raw_input("Enter integer: "))
a = 0

# loop until find cube root or pass input
while a**3 < abs(x):
    a = a + 1

# passed input
if a**3 != abs(x):
    print x, "is not a perfect cube."

else:
    if x < 0:
        a = -a;

    print "Cube root of", x ,"is", a
