# Approach 1
# def findMissingRepeatingNumbers(a: [int]) -> [int]:
#     n = len(a)
#     s = sum(a)
#     sn = n*(n+1)/2
#     s2 = 0
#     for i in a:
#         s2 += (i*i)
    
#     s2n = (n*(n+1)*((2*n)+1))/6

#     x = int(1/2 * (((s2-s2n)/(s-sn)) + (s-sn)))
#     y = int(x - (s-sn))

#     return [x, y]

# Approach 2
def findMissingRepeatingNumbers(a: [int]) -> [int]:
    # Write your code here
    xor = 0
    for i in range(len(a)):
        xor = xor ^ (i+1) ^ a[i]

    d_bit = 0
    while (xor & (1 << d_bit)) == 0:
        d_bit += 1
    
    g0 = 0
    g1 = 0
    for i in range(len(a)):
        if (i+1) & (1 << d_bit) > 0:
            g1 = g1 ^ (i+1)
        else:
            g0 = g0 ^ (i+1)
        
        if a[i] & (1 << d_bit) > 0:
            g1 = g1 ^ a[i]
        else:
            g0 = g0 ^ a[i]

    if g1 in a:
        return [g1, g0]
    else:
        return [g0, g1]


a = [1, 4 ,2, 2 ]
print(findMissingRepeatingNumbers(a))
