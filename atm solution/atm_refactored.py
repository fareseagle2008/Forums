# declaring vars
balance = 500
validVlaues = [100,50,10,5,2,1]

def withdraw (balance, request) :
    currentBalance = balance - request
    print ("Current balance =",balance)
    
    #edge cases tests
    if request > balance :
        print ("Can't give you all this money !!")
    elif request <= 0:
        print 'invalid request'
    else:
    #iterating over given vals
    for index in validVlaues :
        # iterating over every val until not valid
        while request - index >= 0 :
                print ("give " + str(index))
                request -= index # updatng request value
    return currentBalance


balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)
