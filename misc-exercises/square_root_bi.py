# Problem Set 0
# Name: A C
# Collaborators: none
# Time Spent: 3:30

def withinEpsilon(a, b, epsilon):
""" Returns bool on whether difference between a and b is within epsilon"""
    if abs(a-b) >= epsilon:
        return False222
    else:
	return True

x = float(raw_input("Enter x: "))
lowBound = 0.0
upBound = max(x, 1.0)
epsilon = 0.01
i = 0

a = upBound / 2.0

# loop until find cube root or pass input
while not withinEpsilon(a**2, x, epsilon) and a <= upBound:
    if a**2 > x:
        upBound = a
    else:
        lowBound = a

    # condition where stuck in loop 
    if upBound == lowBound:
       break

    a = (upBound+lowBound)/2.0
    i += 1
    print i, ": a:,", a
    print lowBound, "-", upBound

print "Iterations: ", i

if withinEpsilon(a**2, x, epsilon):
    print a, "is close to the square root of", x
else:
    print "Failed on square root of", x

