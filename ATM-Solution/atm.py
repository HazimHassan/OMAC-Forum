def withdraw(R, C):
    if R > C:
        print "$500 max"
    elif R <= 0:
        print "Invalid request"
    else:
        while R > 0:
            if R >= 100:
                R = R - 100
                print "give $100"
            elif R >= 50:
                R = R - 50
                print"give $50"
            elif R >= 20:
                R = R - 20
                print"give $20"
            elif R >= 10:
                R = R - 10
                print"give $10"
            elif R >= 5:
                R = R - 5
                print"give $5"
            else:
                R = R - 1
                print"give $1"
print withdraw(100, 500)
