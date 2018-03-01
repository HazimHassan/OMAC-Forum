class ATM():

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        if request > self.balance:
            print "Welcome to " +(self.bank_name)
            print "$"+str(self.balance)+" max"
            print "************************** "
            return self.balance
        elif request <= 0:
            print "Welcome to " +(self.bank_name)
            print "Invalid request"
            print "************************** "
            return self.balance
        else:
            print "Welcome to " +(self.bank_name)
            (self.balance) -= request
            while request > 0:
                if request >= 100:
                    request -= 100
                    print "give $100"
                elif request >= 50:
                    request -= 50
                    print"give $50"
                elif request >= 20:
                    request -= 20
                    print"give $20"
                elif request >= 10:
                    request -= 10
                    print"give $10"
                elif request >= 5:
                    request -= 5
                    print"give $5"
                else:
                    request -= 1
                    print"give $1"
            print "Current Balance " + "$" + str(self.balance)
            print "************************** "
            return self.balance

BALANCE1 = 500
ATM1 = ATM(BALANCE1, "Smart Bank")

BALANCE2 = 1000
ATM2 = ATM(BALANCE2, "Baraka Bank")

ATM1.withdraw(277)
ATM1.withdraw(800)

ATM2.withdraw(100)
ATM2.withdraw(2000)
