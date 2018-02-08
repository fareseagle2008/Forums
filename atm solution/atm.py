# declaring vars
money = 500
request = 228
pvals = [100,50,10,5,2,1]

#iterating over given vals
for index in pvals :
    # iterating over every val until not valid
    while request - index >= 0 :
            print ("give " + str(index))
            request -= index # updatng request value