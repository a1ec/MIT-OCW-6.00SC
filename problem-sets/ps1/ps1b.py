# Problem Set 1 
# Name: AC 
# Collaborators: 
# Time Spent: 3:30
#

bal_outs = int(raw_input("Enter the outstanding balance on your credit card: "))
interest_rate_annual = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
interest_rate_monthly = interest_rate_annual / 12.0

PAYMENT_INCR = 10

i = 0

min_payment_monthly = 0
found_repayment = False
balance = 0

while found_repayment == False:
    min_payment_monthly += PAYMENT_INCR
    bal_prev = bal_outs

    i = 1
    for i in range(1,13):
        balance = bal_prev * (1 + interest_rate_monthly) - min_payment_monthly

        if (balance <= 0):
            found_repayment = True
            break

        bal_prev = balance

print "RESULT"
print "Monthly payment to pay off debt in 1 year: %d" % min_payment_monthly
print "Number of months needed: %d" % i
print "Balance: %.2f" % balance
