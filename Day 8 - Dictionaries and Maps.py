# Task 
# Given n names and phone numbers, assemble a phone book that maps friends'
# names to their respective phone numbers. You will then be given an unknown
# number of names to query your phone book for. For each name queried, print the
# associated entry from your phone book on a new line in the form name=phoneNumber;
# if an entry for names is not found, print 'Not found' instead.



#Solution
n = int(input())
contacts={}
for i in range(n):
    name, number = input().split()
    contacts[name]=number
    
while (True):
    queryname = input()
    try:
        print(queryname + "=" + contacts[queryname])
    except:
        print ('Not found')


