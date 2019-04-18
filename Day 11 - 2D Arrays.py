# Task 
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

#SOLUTION
if __name__ == '__main__':
    arr = []
    total = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(4):
        for j in range(4):
            total.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            
    print(max(total))