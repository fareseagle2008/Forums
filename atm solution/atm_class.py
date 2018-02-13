class ATM:

    def __init__(self, balance, bank_name):
        #self.balance = balance
        self.bank_name = bank_name
        self.balance_history = [balance]

    def withdraw(self, request):

        valid_values = [100, 50, 10, 5, 2, 1]
        current_balance = self.balance_history[len(self.balance_history)-1]-request

        print("Welcome to",self.bank_name)
        print("Current balance =", self.balance_history[-1])
        print("==================================")

        # edge cases tests
        if request > self.balance_history[-1]:
            print("Can't give you all this money !!")
        elif request <= 0:
            print('invalid request')
        else:
            self.balance_history.append(self.balance_history[-1]-request)
            #print("==================================\n",self.balance_history,"\n==================================")
            # iterating over given values
            for index in valid_values:
                # iterating over every val until not valid
                while request - index >= 0:
                    print("give " + str(index))
                    request -= index  # updating request value
        print("==================================")
        return current_balance


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
