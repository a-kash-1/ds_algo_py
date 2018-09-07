import CreditCard.py
class PredatoryCreditCard(CreditCard):
    """For Interest and Fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance"""
        """The initial balance is zero.
        
        customer the name of the customer
        bank - name of the bank
        acnt - the account identifier
        limit - credit limit 
        apr - annual percentage"""


        def charge(self, price):
            """Charge given price to the card, assuming sufficient credit limit

            Return True if charge was processed
            Return False and assess $5 if charge is denied"""

            success = super().charge(price)
            if not success:
                self._balance += 5
            return success

        def process_month(self):
            """Assess monthly interest on outstanding balance."""

            if self._balnce >0:
                # if positive balance, convert APR to monthly multiplicative factor
                monthly_factor = pow(1 + self._apr, 1/12)
                self.balance *= monthly_factor
