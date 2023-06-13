Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('This progam calculates the monthly payment for a fixed-rate mortgage')
print('using an amortization calculator. In order to do this, we will need ')
print('the principal, annual interest rate, and the term (years) of the loan.')

# INPUT SECTION
# TODO: Input the three input variables listed in the comments (program analysis) above.
# Note the principal and interest rate are floats while years is an integers.
annual_rate = float(input("Please enter the interest rate (APR): "))
principal = float(input("Please enter the principal balance: "))
years = int(input("Please enter the term in years: "))

# PROCESSING SECTION
num_payments = years * 12;
monthly_rate = annual_rate / 1200;
# TODO: Write the annuity formula on the instructions in Python using the appropriate variables.
monthly_payment = principal * (monthly_rate + (monthly_rate / ((pow(1 + monthly_rate , num_payments)) - 1)))

# OUTPUT SECTION
print()	
print('Your monthly payment will be: ${:,.2f}'.format(monthly_payment))
