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
    for line in customer_orders:          # i also abbreviate 'customer' as 'cust'
        line = line.rstrip()
        info = line.split('|')            # info = ['rando #', 'customer_name', 'cust_melon_qty', 'cust_paid']

        info.pop(0)                       # if rando # is needed after all, also have to change all info[index values]

        customer_name, cust_melon_qty, cust_paid = info

        print customer_name, cust_melon_qty, cust_paid


current_accounts_receivable("customer-orders.txt")
