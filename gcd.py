#find gcd of two numbers ( greatest common divisor )

#method 1
import math

a = 56
b = 98

gcd = math.gcd( a, b)
print(gcd)

#method 2

a = 56
b = 98

while b:
    a,b = b, a%b
print(f"GCD - {a}")
