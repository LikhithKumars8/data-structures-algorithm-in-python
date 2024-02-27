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