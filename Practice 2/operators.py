# Arithmetic Operators
"""
+	Addition	x + y
-	Subtraction	x - y
*	Multiplication	x * y
/	Division	x / y
%	Modulus	x % y
**	Exponentiation	x ** y
//	Floor division	x // y
"""
x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Assignment Operators
"""
= - x = 5	
+=	-->	x = x + 3	
-=	-->	x = x - 3	
*=	-->	x = x * 3	
/=	-->	x = x / 3	
%=	-->	x = x % 3	
//=	-->	x = x // 3	
**=	-->	x = x ** 3	
&=	-->	x = x & 3	
|=	-->	x = x | 3	
^=	-->	x = x ^ 3	
>>=	-->	x = x >> 3	
<<=	-->	x = x << 3
"""

# Comparison Operators
"""
Operator	Name	Example
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical operators
"""
Operator	Description	Example
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not (x < 5 and x < 10)
"""
x = 5
print(x > 0 and x < 10)

#Identify operators
""""
Operator	Description	Example	
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)

#Difference between is and ==
"""
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal
"""
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# Membership Operators
"""
Operator	Description	Example
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
"""
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # returns True

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits) # returns True

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

#Bitwise operators
"""
Operator Example	
& 	AND	  	x & y	
|	OR	x | y	
^	XOR	x ^ y	
~	NOT ~x	
<<	x << 2	
>>	x >> 2
"""

print(4 & 3)
print(4 | 3)
print(4 ^ 3)
