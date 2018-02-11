
balance = 500
validVlaues = [100,50,10,5,2,1]

def getRequest(balance) :
    while True :
        request = int(input("How Much ? "))
        if request > balance :
            print ("Can't give you all this money !!")
        elif (request <= 0) :
            print ("Are you joking !!")
        else :
            break
    return request

def withdraw (balance, request) :
    currentBalance = balance - request
    print ("Current balance =",balance)
    
    if request > balance :
        print ("Can't give you all this money !!")
        return
       
    #iterating over given values
    for index in validVlaues :
        # iterating over every val until not valid
        while request - index >= 0 :
                print ("give " + str(index))
                request -= index # updatng request value
    return currentBalance


balance = withdraw(balance, getRequest(balance))
