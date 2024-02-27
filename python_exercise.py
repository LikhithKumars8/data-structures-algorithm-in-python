"""
Two loops are running in the below program the first loops time complexity will be
O(n) and the second loops time complexity is also O(n) when added together they become
O(n+n) -> O(2n) if multiplicative constant is removed then it will become O(n). 
"""
l = [1, 2, 3, 4, 5]
sum = 0

for n in l:
    sum += n
print(sum)

product = 1
for i in l:
    product *= i
print(product)

"""
If there is nested loops the order of growth is always O(n) X O(n) => O(n^2).
As for linear search the order of growth is always O(n) more the number of inputs the output time will increase.
"""

"""
The order of growth being log of n
for every increase in 100 -> 1000 -> 100000 the output will increase by one
"""
def int_to_str(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i // 10
        return result
    
print(int_to_str(123))

"""
n log n order of growth
the first loop with n/2 and the other with log n
the binary search has log n order of growth
"""

"""
Referring the below program:
The first loop has O(n) order of growth and the second loop has O(n-1)
as it is a nested loop the O(n) X O(n-1) which will be O(n^2-n) so smaller factor will be eligible to 
be removed and then it will be of the factor O(n^2)
"""
L = [1, 2, 3, 4, 5, 6]

for i in range(0, len(L)):
    for n in range(i+1, len(L)):
        print(f"{L[i]}, {L[n]}")

"""
The below program has two list assigned the first one will run the loop 4 times and the second
will run the loop 5 times which in this case can be represented as O(a X b) if other option which 
can be used to present the order of growth is O(n^2)
"""
A = [1, 2, 3, 4]
B = [2, 3, 4, 5, 6]

for i in A:
    for j in B:
        if i < j:
            print(f"{i, j}")
