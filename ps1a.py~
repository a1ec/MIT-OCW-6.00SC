# Problem Set 1 
# Name: AC 
# Collaborators: 
# Time Spent: 3:30
#

bal_outs = int(raw_input("Enter the outstanding balance on your credit card: "))
interest_rate_annual = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
min_payment_rate_monthly = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))

interest_rate_monthly = interest_rate_annual / 12.0
total_paid = 0
i = 1
for i in range(1,13):
    print "Month: %d" % i

    min_payment_monthly = bal_outs * min_payment_rate_monthly
    print "Minimum monthly payment: $%.2f" % min_payment_monthly 

    interest_instalment = bal_outs * interest_rate_monthly
    principle_paid = min_payment_monthly - interest_instalment
    print "Principle paid: $%.2f" % principle_paid

    bal_outs -= principle_paid
    print "Remaining balance: $%.2f" % bal_outs

    total_paid += min_payment_monthly

print "RESULT"
print "Total amount paid: $%.2f" % total_paid
print "Remaining balance: $%.2f" % bal_outs
