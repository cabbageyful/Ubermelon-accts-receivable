melon_cost = 1.00


def current_accounts_receivable(path):

    """Creates report of all customers with any balance.

    Requires input of the file path to the .txt file with customer orders.
    Set up to read format of customer order file as follows:
    32|Doris Castillo|84|84.0
    Will eliminate the 1st # preceeding the customer's name - irrelevant.
    Will return a report that states '(Customer) owed x, paid y. Balance is z'
    """

    customer_orders = open(path)
    for line in customer_orders:          # I also abbreviate 'customer' as 'cust'
        line = line.rstrip()
        info = line.split('|')            # info = ['rando #', 'customer_name', 'cust_melon_qty', 'cust_paid']

        info.pop(0)                       # if rando # is needed after all, also have to change line 30

        customer_name, cust_melon_qty, cust_paid = info    # assigning respective variable names

        cust_melon_qty = float(cust_melon_qty)
        cust_paid = float(cust_paid)                       # typecasts as floats

        customer_invoice = float(cust_melon_qty) * float(melon_cost)     # customer's total balance

        customer_balance = customer_invoice % cust_paid    # stores the difference btwen amt paid & owed

        if customer_invoice != cust_paid:
            print '{} owed {}, paid {}. Balance is {}'.format(
                customer_name, customer_invoice, cust_paid, customer_balance)


current_accounts_receivable("customer-orders.txt")
