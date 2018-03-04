class ATM():

    def __init__(self, balance, bank_name):
        self.withdrawals_list = []
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        print "Welcome to " +(self.bank_name)
        print "Current balance = " + str(self.balance)
        if request > self.balance:
            print "$"+str(self.balance)+" max"
            print "************************** "
        elif request <= 0:
            print "Invalid request"
            print "************************** "        
        else:
            self.withdrawals_list.append(request)
            self.balance -= request
            ATM.process_request(self, request)

    def process_request(self, request):

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
        print "************************** "
        return self.balance

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print withdrawal

BALANCE1 = 500
ATM1 = ATM(BALANCE1, "Smart Bank")

BALANCE2 = 1000
ATM2 = ATM(BALANCE2, "Baraka Bank")

ATM1.withdraw(277)
ATM1.withdraw(800)

ATM2.withdraw(100)
ATM2.withdraw(2000)

print "ATM 1 withdrawals:"
ATM1.show_withdrawals()
print "ATM 2 withdrawals:"
ATM2.show_withdrawals()
