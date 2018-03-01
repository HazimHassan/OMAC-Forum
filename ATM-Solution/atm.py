def withdraw(request, balance):
    if request > balance:
        print "$"+str(balance)+" max"
        print "************************** "
        return balance
    elif request <= 0:
        print "Invalid request"
        print "************************** "
        return balance
    else:
        balance -= request
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
        print "Current Balance " + "$" + str(balance)
        print "************************** "
        return balance

balance = 500
print "Current Balance " + "$" + str(balance)

balance = withdraw(277, balance)

balance = withdraw(30, balance)

balance = withdraw(5, balance)

balance = withdraw(500, balance)
