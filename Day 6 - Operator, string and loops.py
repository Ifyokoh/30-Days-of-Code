#Task
#Given a string, S, of length N that is indexed from 0 to N - 1, print its
#even-indexed and odd-indexed characters as 2 space-separated strings on a
#single line 


#Solution
S = input()
result = ""
value = ""
for i in range(len(S)):
    if i % 2 == 0:
        result = result + S[i]
for i in range(len(S)):
    if i % 2 != 0:
        value = value + S[i]
print(result,  value)


#Another method
for i in range(int(input())):
    S = input()
    print(S[::2], S[1::2])

#s[::2] what this means is starting from index 0, incrementing
#the index two by two and accessing all even indexes (0,2,4,6, and so on).

#s[1::2] will retrieve all array items, from index 1, incrementing the index
#two by two and accessing all odd indexes (1,3,5,7,9, and so on).
