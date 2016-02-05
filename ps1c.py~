# Problem Set 1 
# Name: AC 
# Collaborators: 
# Time Spent: 3:30
#

def bisection_search():
    pass

# algorithm
# take in upper and lower bound
# while (y != x):
#   start y in middle
#   if y < x
#     low_bound = y
#   if x < y
#     up_bound = y


bal_outs = int(raw_input("Enter the outstanding balance on your credit card: "))
interest_rate_annual = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
interest_rate_monthly = interest_rate_annual / 12.0

min_payment_monthly = 0
balance = 0

MAX_ITER = 300

# set bounds as defined by specs in problem set
bound_lower = bal_outs / 12.0
bound_upper = (bal_outs * (1 + (interest_rate_annual / 12.0)) ** 12.0) / 12.0
tolerance = 0.01

n = 1
while n < MAX_ITER:
    # reset input balance as initial value for brute force approach
    bal_prev = bal_outs

    min_payment_monthly = (bound_lower + bound_upper) / 2.0

    i = 1
    for i in range(1,13):
        balance = bal_prev * (1 + interest_rate_monthly) - min_payment_monthly
        bal_prev = balance

    if abs(balance) <= tolerance:
        found_repayment = True
        break

    # repayments not sufficient, increase
    if balance > 0:
        bound_lower = min_payment_monthly
    else:
        bound_upper = min_payment_monthly

    n += 1

print "RESULT"
print "Monthly payment to pay off debt in 1 year: %.2f" % min_payment_monthly
print "Number of months needed: %d" % i
print "Balance: %.2f" % balance
print "%d iterations attempted" % n
