# counting_sort (계수 정렬)

count = [0,0,0,0,0]

arr = [1,3,2,4,3,
       2,5,3,1,2,
       3,4,4,3,5,
       1,2,3,5,2,
       3,1,4,3,5,
       1,2,1,1,1]

for i in range(0, 30):
    count[arr[i] - 1] = count[arr[i] - 1] + 1

for i in range(0, 5):
    if(count[i] != 0):
        for j in range(0, count[i]):
            print(i+1, end=" ")