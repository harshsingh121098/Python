n = int(input())
k=n-1
for i in range(0,n):
    for j in range(0,n):
        if(j>=k):
            print('#')
    k=k-i
k=n-1
print('\n')
        