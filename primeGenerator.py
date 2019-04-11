__author__ = 'rdhek'

testCases = int(raw_input())
arr = []
flag = 0
for n in range(0,testCases):
    arr.append( map(long,raw_input().split(' ')))

#print arr.__len__()
for noOftest in range(0,arr.__len__()):
    rngstart = arr[noOftest][0]
    if arr[noOftest][0] == 2:
        print int(2)
        rngstart = 3
    if arr[noOftest][0] == 1:
        rngstart = 2

    for n in range(rngstart,arr[noOftest][1] + 1):
        #print "first" , n
        flag = 0
        for k in range(2, n/2 ):
            #print "second" , k
            if (n%k == 0):
                flag = 1
                break
        if flag == 0:
                print n





