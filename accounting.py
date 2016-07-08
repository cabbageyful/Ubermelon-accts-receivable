"""To Do:

Read through accounting.py and understand what it's doing.
Create a function that takes in a text file of customer orders and parses it to produce similar output.
Add comments explaining what your code is doing.
Read over the solution and see how it compairs to your answer."""

melon_cost = 1.00

# rando # | customer_name | cust_melon_quantity | customer_paid
# 32|Doris Castillo|84|84.00

# customer invoice = # of melons * melon cost
# if customer invoice does not equal customer_paid
# print out customer's name, & amounts. (can I do a mod too?!) {:.2f}.format indicates 2 decimal places


def current_accounts_receivable(path):

    """
    """

    customer_orders = open(path)
    for line in customer_orders:          # I also abbreviate 'customer' as 'cust'
        line = line.rstrip()
        info = line.split('|')            # info = ['rando #', 'customer_name', 'cust_melon_qty', 'cust_paid']

        info.pop(0)                       # if rando # is needed after all, also have to change line 30

        customer_name, cust_melon_qty, cust_paid = info    # assigning respective variable names

        cust_melon_qty = float(cust_melon_qty)
        cust_paid = float(cust_paid)

        customer_invoice = cust_melon_qty * float(melon_cost)     # customer's total balance

        customer_balance = float(customer_invoice) % cust_paid    # stores the difference btwen amt paid & owed

        print customer_balance, cust_melon_qty, cust_paid

        # if customer_invoice != cust_paid:
        #    print '{} owed {:2f} and paid {:2f}. Balance is {:2f}'.format(customer_name, customer_invoice, cust_paid, customer_balance)


current_accounts_receivable("customer-orders.txt")
