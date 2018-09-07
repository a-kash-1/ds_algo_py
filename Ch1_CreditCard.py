class CreditCard:
    "A consumer credit card"

    def __init__(self, customer, bank, acnt, limit):
        '''Create new credit card instance

        Initial balance is zero

        customer: the name of customer
        bank: name of bank
        acnt: account identifier
        limit: credit limit(dollars)
        '''

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return(self._customer)

    def get_bank(self):
        return(self._bank)

    def get_account(self):
        return(self._account)

    def get_limit(self):
        return(self._limit)

    def get_balance(self):
        return(self._balance)

    #Up till now was the beginning of the credit card class

    #Now comes the conclusion

    def charge(self, price):
        #Charge given price to card, assuming sufficient credit, True if processed

        if (price + self._balance > self._limit):
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        '''Process customer payment that reduces balance'''
        self.balance -= amount


    #A sample run

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John', 'SBI', '1010 1010 1010 1010', 200))
    wallet.append(CreditCard('Bill', 'SBI', '1110 1010 1010 1010', 300))
    wallet.append(CreditCard('Clinton', 'DDb', '2010 1010 1010 1010', 400))
    wallet.append(CreditCard('Yo', 'PNB', '1010 3010 1010 1010', 500))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer = ', wallet[c].get_customer())

